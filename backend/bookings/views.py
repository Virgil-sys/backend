from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .serializers import BookingSerializer
from .models import Booking


def send_admin_notification_email(booking):
    """Send detailed booking notification to admin"""
    try:
        subject = f"🎉 New Booking Received - {booking.package_title}"
        context = {'booking': booking}

        # Render HTML and plain text content from templates
        html_content = render_to_string('bookings/admin_notification.html', context)
        text_content = strip_tags(html_content) # Generate plain text from HTML
        
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.ADMIN_EMAIL] # Use a setting for the admin email
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False) # Set to False for better error reporting during development
        
    except Exception as e:
        print(f"Error sending admin email: {e}")


def send_customer_confirmation_email(booking):
    """Send confirmation email with bank details to customer"""
    try:
        subject = f"Booking Confirmation - {booking.package_title}"
        context = {
            'booking': booking,
            'bank_details': settings.BANK_DETAILS
        }

        # Render HTML and plain text content from templates
        html_content = render_to_string('bookings/customer_confirmation.html', context)
        text_content = strip_tags(html_content)
        
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[booking.customer.email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False) # Set to False for better error reporting
        
    except Exception as e:
        print(f"Error sending customer email: {e}")


class BookingCreateView(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save()

            # Send enhanced email notifications
            try:
                send_admin_notification_email(booking)
                send_customer_confirmation_email(booking)
            except Exception as e:
                # Keep API resilient even if email fails
                print(f"Email notification error: {e}")

            return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingDetailView(APIView):
    def get(self, request, pk):
        try:
            booking = Booking.objects.select_related('customer').get(pk=pk)
        except Booking.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(BookingSerializer(booking).data)


class BookingStatusView(APIView):
    def get(self, request, pk):
        try:
            booking = Booking.objects.only('id', 'status', 'reference_number').get(pk=pk)
        except Booking.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            "id": booking.id,
            "status": booking.status,
            "reference_number": booking.reference_number,
        })
