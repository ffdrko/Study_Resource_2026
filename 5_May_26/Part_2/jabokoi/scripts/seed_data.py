import os
import sys
import django
from pathlib import Path

# Set up Django environment
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from destinations.models import Destination, Hotel, Activity, TransportRoute

def seed_destinations():
    destinations = [
        {
            "name_en": "Cox's Bazar",
            "name_bn": "কক্সবাজার",
            "division": "Chittagong",
            "type": "beach",
            "description_en": "The world's longest natural sea beach.",
            "description_bn": "বিশ্বের দীর্ঘতম প্রাকৃতিক সমুদ্র সৈকত।",
            "best_months": [10, 11, 12, 1, 2, 3],
            "avoid_months": [6, 7, 8, 9],
            "monsoon_risk": "medium",
            "flood_risk": False,
            "lat": 21.4272,
            "lng": 91.9702,
            "weather_city_id": "1185188",
            "images": ["https://images.unsplash.com/photo-1581442188404-58a43657f202"],
            "tags": ["beach", "family", "sunset"],
            "min_days_recommended": 2,
            "max_days_recommended": 5
        },
        {
            "name_en": "Sylhet",
            "name_bn": "সিলেট",
            "division": "Sylhet",
            "type": "hill",
            "description_en": "Land of two leaves and a bud, famous for tea gardens.",
            "description_bn": "দুটি পাতা একটি কুঁড়ির দেশ, চা বাগানের জন্য বিখ্যাত।",
            "best_months": [10, 11, 12, 1, 2, 3, 4],
            "avoid_months": [6, 7, 8],
            "monsoon_risk": "low",
            "flood_risk": True,
            "lat": 24.8949,
            "lng": 91.8687,
            "weather_city_id": "1185099",
            "images": ["https://images.unsplash.com/photo-1590603740183-980e7f6920eb"],
            "tags": ["tea garden", "nature", "rain"],
            "min_days_recommended": 3,
            "max_days_recommended": 6
        },
        {
            "name_en": "Bandarban",
            "name_bn": "বান্দরবান",
            "division": "Chittagong",
            "type": "hill",
            "description_en": "The roof of Bangladesh, known for its breathtaking hills.",
            "description_bn": "বাংলাদেশের ছাদ, মনোরম পাহাড়ের জন্য পরিচিত।",
            "best_months": [10, 11, 12, 1, 2, 3],
            "avoid_months": [6, 7, 8, 9],
            "monsoon_risk": "high",
            "flood_risk": False,
            "lat": 22.1953,
            "lng": 92.2184,
            "weather_city_id": "1185241",
            "images": ["https://images.unsplash.com/photo-1623504381693-5329b821438a"],
            "tags": ["trekking", "adventure", "hills"],
            "min_days_recommended": 3,
            "max_days_recommended": 5
        }
    ]

    for d_data in destinations:
        dest, created = Destination.objects.get_or_create(
            name_en=d_data['name_en'],
            defaults=d_data
        )
        if created:
            print(f"Created destination: {dest.name_en}")
            # Add some mock hotels for each destination
            Hotel.objects.create(
                destination=dest,
                name=f"Premium Resort {dest.name_en}",
                name_bn=f"প্রিমিয়াম রিসোর্ট {dest.name_bn}",
                star_rating=5,
                price_per_night_bdt=8000,
                price_tier="premium",
                address=f"Beach Road, {dest.name_en}",
                lat=dest.lat,
                lng=dest.lng
            )
            Hotel.objects.create(
                destination=dest,
                name=f"Budget Inn {dest.name_en}",
                name_bn=f"বাজেট ইন {dest.name_bn}",
                star_rating=3,
                price_per_night_bdt=1200,
                price_tier="budget",
                address=f"Main Town, {dest.name_en}",
                lat=dest.lat,
                lng=dest.lng
            )

if __name__ == "__main__":
    seed_destinations()
