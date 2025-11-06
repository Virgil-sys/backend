"""
Script to populate the database with sample activities, transport, and accommodation options.
Run this after migrations: python manage.py shell < populate_activities.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from activities.models import Activity

# Clear existing activities
Activity.objects.all().delete()

# Activities
activities_list = [
    {'activity_id': 'sunset-cruise', 'title': 'Sunset Cruise on Zambezi', 'category': 'activity', 'price': 45, 'duration': '2 hours', 'description': 'Romantic sunset cruise with drinks included'},
    {'activity_id': 'elephant-ride', 'title': 'Elephant Back Safari', 'category': 'activity', 'price': 80, 'duration': '1 hour', 'description': 'Up-close elephant experience'},
    {'activity_id': 'bungee-jump', 'title': 'Victoria Falls Bungee Jump', 'category': 'activity', 'price': 160, 'duration': '30 minutes', 'description': '111m jump from the bridge'},
    {'activity_id': 'white-water', 'title': 'White Water Rafting', 'category': 'activity', 'price': 120, 'duration': 'Full day', 'description': 'Grade 5 rapids adventure'},
    {'activity_id': 'village-tour', 'title': 'Cultural Village Tour', 'category': 'activity', 'price': 35, 'duration': '3 hours', 'description': 'Traditional village experience'},
    {'activity_id': 'helicopter-tour', 'title': 'Helicopter Flight (13 min)', 'category': 'activity', 'price': 136, 'duration': '13 minutes', 'description': 'Aerial view of Victoria Falls'},
    {'activity_id': 'canoe-safari', 'title': 'Canoe Safari', 'category': 'activity', 'price': 65, 'duration': 'Half day', 'description': 'Peaceful wildlife viewing from canoe'},
    {'activity_id': 'fishing-trip', 'title': 'Tiger Fishing', 'category': 'activity', 'price': 90, 'duration': 'Half day', 'description': 'Sport fishing on the Zambezi'},
    {'activity_id': 'zip-line', 'title': 'Zip Line Adventure', 'category': 'activity', 'price': 55, 'duration': '1 hour', 'description': 'Multiple zip lines over the gorge'},
    {'activity_id': 'horse-ride', 'title': 'Horseback Safari', 'category': 'activity', 'price': 75, 'duration': '2 hours', 'description': 'Wildlife viewing on horseback'},
]

# Transport
transport_list = [
    {'activity_id': 'airport-transfer', 'title': 'Airport Transfer (One Way)', 'category': 'transport', 'price': 30, 'description': 'Victoria Falls Airport to hotel'},
    {'activity_id': 'airport-return', 'title': 'Airport Transfer (Return)', 'category': 'transport', 'price': 50, 'description': 'Round trip airport transfers'},
    {'activity_id': 'shuttle-hwange', 'title': 'Shuttle to Hwange National Park', 'category': 'transport', 'price': 85, 'description': 'Private transfer to Hwange'},
    {'activity_id': 'shuttle-chobe', 'title': 'Shuttle to Chobe (Botswana)', 'category': 'transport', 'price': 70, 'description': 'Border crossing included'},
    {'activity_id': 'car-rental-day', 'title': 'Car Rental (Per Day)', 'category': 'transport', 'price': 60, 'description': '4x4 vehicle with insurance'},
    {'activity_id': 'driver-guide', 'title': 'Private Driver/Guide (Full Day)', 'category': 'transport', 'price': 150, 'description': 'Professional driver and guide'},
]

# Accommodation
accommodation_list = [
    {'activity_id': 'budget-hotel', 'title': 'Budget Hotel (Per Night)', 'category': 'accommodation', 'price': 45, 'description': 'Clean, comfortable budget accommodation'},
    {'activity_id': 'mid-range-hotel', 'title': 'Mid-Range Hotel (Per Night)', 'category': 'accommodation', 'price': 90, 'description': '3-star hotel with pool'},
    {'activity_id': 'luxury-lodge', 'title': 'Luxury Lodge (Per Night)', 'category': 'accommodation', 'price': 250, 'description': '5-star lodge with falls view'},
    {'activity_id': 'safari-camp', 'title': 'Safari Camp (Per Night)', 'category': 'accommodation', 'price': 180, 'description': 'Tented camp in bush setting'},
    {'activity_id': 'family-suite', 'title': 'Family Suite (Per Night)', 'category': 'accommodation', 'price': 150, 'description': 'Sleeps 4-6 people'},
    {'activity_id': 'camping-site', 'title': 'Camping Site (Per Night)', 'category': 'accommodation', 'price': 15, 'description': 'Basic camping with facilities'},
]

# Create all activities
all_items = activities_list + transport_list + accommodation_list
created_count = 0

for idx, item in enumerate(all_items):
    Activity.objects.create(
        activity_id=item['activity_id'],
        title=item['title'],
        category=item['category'],
        price=item['price'],
        duration=item.get('duration', ''),
        description=item.get('description', ''),
        is_active=True,
        display_order=idx * 10
    )
    created_count += 1

print(f"✅ Successfully created {created_count} items:")
print(f"   - {len(activities_list)} Activities")
print(f"   - {len(transport_list)} Transport options")
print(f"   - {len(accommodation_list)} Accommodation options")
