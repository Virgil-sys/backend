from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction

from .models import BankAccount, BankTransfer
from .serializers import BankAccountSerializer, ProofUploadSerializer, BankTransferSerializer
from bookings.models import Booking


class BankDetailsView(APIView):
    def post(self, request):
        accounts = BankAccount.objects.filter(is_active=True)
        data = BankAccountSerializer(accounts, many=True).data
        instructions = {
            "message": "Use your booking reference as the payment reference to speed up verification.",
            "deadline_hours": 48,
        }
        return Response({"accounts": data, "instructions": instructions})


class ProofUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = ProofUploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        booking: Booking = serializer.validated_data["booking"]
        f = serializer.validated_data["proof"]
        amount_received = serializer.validated_data.get("amount_received")
        transfer_date = serializer.validated_data.get("transfer_date")

        # Choose an active bank account (first by default)
        acct = BankAccount.objects.filter(is_active=True).first()

        bt = BankTransfer.objects.create(
            booking=booking,
            bank_name=acct.bank_name if acct else "",
            account_name=acct.account_name if acct else "",
            account_number=acct.account_number if acct else "",
            branch_code=acct.branch_code if acct else "",
            reference_number=booking.reference_number,
            amount_expected=booking.total_amount,
            amount_received=amount_received,
            transfer_date=transfer_date,
            proof_of_payment=f,
        )

        return Response({
            "message": "Proof uploaded. We will verify your payment shortly.",
            "transfer": BankTransferSerializer(bt).data,
        }, status=status.HTTP_201_CREATED)


class PaymentStatusView(APIView):
    def get(self, request, booking_id: int):
        try:
            booking = Booking.objects.get(pk=booking_id)
        except Booking.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        last_transfer = booking.bank_transfers.order_by('-created_at').first()
        return Response({
            "booking_id": booking.id,
            "booking_status": booking.status,
            "payment_status": last_transfer.status if last_transfer else None,
            "reference_number": booking.reference_number,
        })


# Admin endpoints
class AdminBookingsListView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        qs = Booking.objects.select_related('customer').all()
        status_param = request.GET.get('status')
        if status_param:
            qs = qs.filter(status=status_param)
        data = [
            {
                "id": b.id,
                "customer": {
                    "id": b.customer_id,
                    "name": b.customer.name,
                    "email": b.customer.email,
                },
                "package_title": b.package_title,
                "total_amount": str(b.total_amount),
                "status": b.status,
                "payment_method": b.payment_method,
                "reference_number": b.reference_number,
                "created_at": b.created_at,
            }
            for b in qs.order_by('-created_at')
        ]
        return Response(data)


class AdminPendingPaymentsView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        qs = BankTransfer.objects.filter(status=BankTransfer.Status.PENDING).select_related('booking', 'booking__customer')
        return Response(BankTransferSerializer(qs, many=True).data)


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

class AdminVerifyPaymentView(APIView):
    permission_classes = [permissions.IsAdminUser]

    @transaction.atomic
    def post(self, request, booking_id: int):
        try:
            booking = Booking.objects.select_for_update().get(pk=booking_id)
        except Booking.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        transfer = booking.bank_transfers.order_by('-created_at').first()
        if not transfer:
            return Response({"detail": "No transfer found"}, status=status.HTTP_400_BAD_REQUEST)

        transfer.mark_verified(user=request.user if request.user.is_authenticated else None)
        booking.status = Booking.Status.CONFIRMED
        booking.save(update_fields=["status"])

        # Send confirmation email
        try:
            customer_email = booking.customer.email
            if customer_email:
                subject = f"Payment Confirmed for Your Prairies Africa Booking (Ref: {booking.reference_number})"
                
                context = {
                    'customer_name': booking.customer.name,
                    'booking_reference': booking.reference_number,
                    'package_title': booking.package_title,
                    'number_of_people': booking.number_of_people,
                    'preferred_date': booking.preferred_date.strftime('%d %B %Y') if booking.preferred_date else 'N/A',
                    'total_amount': booking.total_amount,
                }
                
                # Simple text email
                message = render_to_string('emails/payment_confirmed.txt', context)
                
                # HTML email (optional, requires template)
                # html_message = render_to_string('emails/payment_confirmed.html', context)
                
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [customer_email],
                    # html_message=html_message,
                    fail_silently=False,
                )
        except Exception as e:
            # Log the error but don't fail the request
            print(f"Error sending payment confirmation email for booking {booking.id}: {e}")

        return Response({"message": "Payment verified and booking confirmed."})

# Create your views here.
