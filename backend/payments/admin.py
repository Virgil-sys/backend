from django.contrib import admin
from .models import BankAccount, BankTransfer


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ("id", "bank_name", "account_name", "account_number", "currency", "is_active")
    search_fields = ("bank_name", "account_name", "account_number", "swift_code")
    list_filter = ("currency", "is_active")


@admin.register(BankTransfer)
class BankTransferAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "booking",
        "reference_number",
        "amount_expected",
        "amount_received",
        "status",
        "transfer_date",
        "verified_by",
        "verified_at",
    )
    list_filter = ("status", "transfer_date", "verified_at")
    search_fields = ("reference_number", "booking__reference_number", "booking__customer__name")

# Register your models here.
