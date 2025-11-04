from rest_framework import serializers
from .models import Activity, BookingActivity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'activity_id', 'title', 'category', 'description', 'price', 'duration', 'is_active']


class BookingActivitySerializer(serializers.ModelSerializer):
    activity_details = ActivitySerializer(source='activity', read_only=True)
    
    class Meta:
        model = BookingActivity
        fields = ['id', 'activity', 'activity_details', 'quantity', 'subtotal']
        read_only_fields = ['subtotal']
