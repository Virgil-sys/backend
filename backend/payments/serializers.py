from rest_framework import serializers
from .models import BankAccount, BankTransfer
from bookings.models import Booking


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = [
            "id",
            "bank_name",
            "account_name",
            "account_number",
            "branch_code",
            "swift_code",
            "currency",
            "notes",
        ]


class BankTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransfer
        fields = [
            "id",
            "booking",
            "bank_name",
            "account_name",
            "account_number",
            "branch_code",
            "reference_number",
            "amount_expected",
            "amount_received",
            "transfer_date",
            "status",
            "proof_of_payment",
            "verified_by",
            "verified_at",
            "created_at",
        ]
        read_only_fields = [
            "status",
            "verified_by",
            "verified_at",
            "created_at",
            "amount_expected",
        ]


class ProofUploadSerializer(serializers.Serializer):
    booking_id = serializers.IntegerField(required=False)
    reference_number = serializers.CharField(required=False)
    amount_received = serializers.DecimalField(max_digits=12, decimal_places=2, required=False)
    transfer_date = serializers.DateField(required=False)
    proof = serializers.FileField()

    def validate(self, attrs):
        booking = None
        ref = attrs.get("reference_number")
        bid = attrs.get("booking_id")
        if not ref and not bid:
            raise serializers.ValidationError("Provide booking_id or reference_number")
        try:
            if bid:
                booking = Booking.objects.get(pk=bid)
            else:
                booking = Booking.objects.get(reference_number=ref)
        except Booking.DoesNotExist:
            raise serializers.ValidationError("Booking not found")
        attrs["booking"] = booking

        f = attrs.get("proof")
        if f:
            if f.size > 5 * 1024 * 1024:
                raise serializers.ValidationError("File too large (max 5MB)")
            allowed = {"image/jpeg", "image/png", "application/pdf"}
            if getattr(f, "content_type", None) not in allowed:
                raise serializers.ValidationError("Unsupported file type. Use JPG, PNG, or PDF.")
        return attrs
