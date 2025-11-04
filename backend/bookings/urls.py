from django.urls import path
from .views import BookingCreateView, BookingDetailView, BookingStatusView

urlpatterns = [
    path('create/', BookingCreateView.as_view(), name='booking-create'),
    path('<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('<int:pk>/status/', BookingStatusView.as_view(), name='booking-status'),
]
