from django.db import models
from django.utils import timezone

from customers.models import Customer


class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'
        COMPLETED = 'completed', 'Completed'

    class PaymentMethod(models.TextChoices):
        BANK_TRANSFER = 'bank_transfer', 'Bank Transfer'
        CASH = 'cash', 'Cash'
        CARD = 'card', 'Card'

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')

    package_id = models.CharField(max_length=100)
    package_title = models.CharField(max_length=255)
    package_price = models.DecimalField(max_digits=12, decimal_places=2)

    # Optional additional activity
    additional_activity_id = models.CharField(max_length=100, blank=True)
    additional_activity_title = models.CharField(max_length=255, blank=True)
    additional_activity_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    number_of_people = models.PositiveIntegerField(default=1)
    preferred_date = models.DateField(null=True, blank=True)
    special_requests = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices, default=PaymentMethod.BANK_TRANSFER)

    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    payment_deadline = models.DateTimeField(null=True, blank=True)
    reference_number = models.CharField(max_length=50, blank=True, db_index=True)

    def save(self, *args, **kwargs):
        # Calculate total: base package + additional activity
        base_total = (self.package_price or 0) * self.number_of_people
        additional_total = (self.additional_activity_price or 0) * self.number_of_people
        self.total_amount = base_total + additional_total

        if not self.payment_deadline:
            self.payment_deadline = timezone.now() + timezone.timedelta(hours=48)
        
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        # Generate a unique reference number after the object has a primary key
        if is_new:
            self.reference_number = f"BK-{timezone.now().strftime('%Y%m%d')}-{self.pk}"
            super().save(update_fields=['reference_number'])

    def __str__(self) -> str:
        return f"Booking #{self.pk} - {self.package_title} for {self.customer.name}"

# Create your models here.
