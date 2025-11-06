from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "colored_status",
        "customer_name_link",
        "customer_email",
        "package_title",
        "number_of_people",
        "total_amount_display",
        "payment_method",
        "reference_number",
        "payment_deadline_display",
        "created_at",
    )
    list_filter = ("status", "payment_method", "created_at", "preferred_date")
    search_fields = ("reference_number", "package_title", "customer__name", "customer__email")
    readonly_fields = ("reference_number", "created_at", "updated_at", "total_amount")
    list_editable = ()  # Removed to fix error
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    
    fieldsets = (
        ("📋 Booking Information", {
            "fields": ("reference_number", "status", "created_at", "updated_at")
        }),
        ("👤 Customer Details", {
            "fields": ("customer",)
        }),
        ("📦 Package Details", {
            "fields": (
                "package_id",
                "package_title",
                "package_price",
                "additional_activity_id",
                "additional_activity_title",
                "additional_activity_price",
                "number_of_people",
                "preferred_date",
            )
        }),
        ("💰 Payment Information", {
            "fields": ("total_amount", "payment_method", "payment_deadline")
        }),
        ("📝 Additional Information", {
            "fields": ("special_requests",),
            "classes": ("collapse",)
        }),
    )

    def customer_name_link(self, obj):
        if not obj.customer:
            return "—"
        url = reverse("admin:customers_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', url, obj.customer.name)
    customer_name_link.short_description = "Customer"
    customer_name_link.admin_order_field = "customer__name"

    def customer_email(self, obj):
        return obj.customer.email if obj.customer else "—"
    customer_email.short_description = "Email"
    customer_email.admin_order_field = "customer__email"

    
    def colored_status(self, obj):
        """Display status with color coding"""
        colors = {
            'pending': '#f59e0b',  # amber
            'confirmed': '#10b981',  # green
            'cancelled': '#ef4444',  # red
            'completed': '#3b82f6',  # blue
        }
        color = colors.get(obj.status, '#6b7280')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold; font-size: 11px;">{}</span>',
            color,
            obj.get_status_display().upper()
        )
    colored_status.short_description = "Status"
    colored_status.admin_order_field = "status"
    
    def total_amount_display(self, obj):
        """Display total amount with currency symbol"""
        return format_html(
            '<span style="color: #f59e0b; font-weight: bold; font-size: 14px;">${}</span>',
            obj.total_amount
        )
    total_amount_display.short_description = "Total"
    total_amount_display.admin_order_field = "total_amount"
    
    def payment_deadline_display(self, obj):
        """Display payment deadline with urgency indicator"""
        if not obj.payment_deadline:
            return "—"
        
        from django.utils import timezone
        now = timezone.now()
        
        if obj.payment_deadline < now and obj.status == 'pending':
            # Overdue
            return format_html(
                '<span style="color: #ef4444; font-weight: bold;">⚠️ {}</span>',
                obj.payment_deadline.strftime('%Y-%m-%d %H:%M')
            )
        elif obj.payment_deadline < now + timezone.timedelta(hours=6) and obj.status == 'pending':
            # Soon
            return format_html(
                '<span style="color: #f59e0b; font-weight: bold;">⏰ {}</span>',
                obj.payment_deadline.strftime('%Y-%m-%d %H:%M')
            )
        else:
            return obj.payment_deadline.strftime('%Y-%m-%d %H:%M')
    
    payment_deadline_display.short_description = "Deadline"
    payment_deadline_display.admin_order_field = "payment_deadline"
    
    actions = ["mark_as_confirmed", "mark_as_pending", "mark_as_cancelled"]
    
    def mark_as_confirmed(self, request, queryset):
        updated = queryset.update(status='confirmed')
        self.message_user(request, f"{updated} booking(s) marked as confirmed.")
    mark_as_confirmed.short_description = "✅ Mark selected as Confirmed"
    
    def mark_as_pending(self, request, queryset):
        updated = queryset.update(status='pending')
        self.message_user(request, f"{updated} booking(s) marked as pending.")
    mark_as_pending.short_description = "⏳ Mark selected as Pending"
    
    def mark_as_cancelled(self, request, queryset):
        updated = queryset.update(status='cancelled')
        self.message_user(request, f"{updated} booking(s) marked as cancelled.")
    mark_as_cancelled.short_description = "❌ Mark selected as Cancelled"

# Register your models here.
