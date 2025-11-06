from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from bookings.models import Booking


def proof_upload_path(instance: "BankTransfer", filename: str) -> str:
    # Store proofs under media/proofs/<booking_id>/timestamp_filename
    ts = timezone.now().strftime('%Y%m%d%H%M%S')
    return f"proofs/{instance.booking_id or 'unassigned'}/{ts}_{filename}"


class BankAccount(models.Model):
    bank_name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=50, blank=True)
    swift_code = models.CharField(max_length=50, blank=True)
    currency = models.CharField(max_length=10, default="ZAR")
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.bank_name} - {self.account_number} ({self.currency})"


class BankTransfer(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        VERIFIED = 'verified', 'Verified'
        FAILED = 'failed', 'Failed'

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='bank_transfers')

    bank_name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=50, blank=True)
    reference_number = models.CharField(max_length=100, db_index=True)

    amount_expected = models.DecimalField(max_digits=12, decimal_places=2)
    amount_received = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    transfer_date = models.DateField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    proof_of_payment = models.FileField(upload_to=proof_upload_path, blank=True)

    verified_by = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL, related_name='verified_transfers')
    verified_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_verified(self, user=None):
        self.status = self.Status.VERIFIED
        self.verified_by = user
        self.verified_at = timezone.now()
        self.save(update_fields=['status', 'verified_by', 'verified_at'])

    def __str__(self) -> str:
        return f"Transfer for Booking {self.booking_id} - {self.reference_number} ({self.status})"

# Create your models here.
