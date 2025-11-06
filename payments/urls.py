from django.urls import path
from .views import (
    BankDetailsView,
    ProofUploadView,
    PaymentStatusView,
    AdminBookingsListView,
    AdminPendingPaymentsView,
    AdminVerifyPaymentView,
)

urlpatterns = [
    # Public/payment endpoints
    path('bank-details/', BankDetailsView.as_view(), name='bank-details'),
    path('upload-proof/', ProofUploadView.as_view(), name='upload-proof'),
    path('payment-status/<int:booking_id>/', PaymentStatusView.as_view(), name='payment-status'),

    # Admin endpoints
    path('admin/bookings/', AdminBookingsListView.as_view(), name='admin-bookings-list'),
    path('admin/payments/pending/', AdminPendingPaymentsView.as_view(), name='admin-pending-payments'),
    path('admin/bookings/<int:booking_id>/verify-payment/', AdminVerifyPaymentView.as_view(), name='admin-verify-payment'),
]
