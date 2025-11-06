from django.db import models


class ActivityCategory(models.TextChoices):
    PACKAGE = 'package', 'Package'
    ACTIVITY = 'activity', 'Activity'
    TRANSPORT = 'transport', 'Transport'
    ACCOMMODATION = 'accommodation', 'Accommodation'


class Activity(models.Model):
    """Represents any bookable item: packages, activities, transport, accommodation"""
    
    activity_id = models.CharField(max_length=100, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=ActivityCategory.choices, default=ActivityCategory.ACTIVITY)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    duration = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['category', 'display_order', 'title']
        verbose_name_plural = 'Activities'
    
    def __str__(self):
        return f"{self.get_category_display()}: {self.title} (${self.price})"


class BookingActivity(models.Model):
    """Links bookings to multiple activities"""
    
    booking = models.ForeignKey('bookings.Booking', on_delete=models.CASCADE, related_name='booking_activities')
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)  # For number of people
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    
    class Meta:
        unique_together = ['booking', 'activity']
    
    def save(self, *args, **kwargs):
        # Auto-calculate subtotal
        self.subtotal = self.activity.price * self.quantity
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.booking.reference_number} - {self.activity.title}"
