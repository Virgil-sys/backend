from rest_framework import serializers
from customers.models import Customer
from django.conf import settings
from .models import Booking


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "name", "email", "phone", "customer_notes"]


class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Booking
        fields = [
            "id",
            "customer",
            "package_id",
            "package_title",
            "package_price",
            "additional_activity_id",
            "additional_activity_title",
            "additional_activity_price",
            "number_of_people",
            "preferred_date",
            "special_requests",
            "status",
            "payment_method",
            "total_amount",
            "created_at",
            "updated_at",
            "payment_deadline",
            "reference_number",
        ]
        read_only_fields = [
            "status",
            "total_amount",
            "created_at",
            "updated_at",
            "payment_deadline",
            "reference_number",
        ]

    def create(self, validated_data):
        customer_data = validated_data.pop("customer")
        customer, _ = Customer.objects.get_or_create(
            email=customer_data["email"], defaults=customer_data
        )
        # Update customer details if provided
        for key in ["name", "phone", "customer_notes"]:
            if key in customer_data and customer_data[key]:
                setattr(customer, key, customer_data[key])
        customer.save()

        # --- Price Security Enhancement ---
        # Ignore price from frontend; get it from settings based on package_id.
        package_id = validated_data.get("package_id")
        package_info = settings.PACKAGE_PRICES.get(package_id)

        if package_info:
            validated_data["package_price"] = package_info['price']
            validated_data["package_title"] = package_info['title']
        # ------------------------------------

        booking = Booking.objects.create(customer=customer, **validated_data)
        return booking
