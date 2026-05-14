from django.db import models
import uuid

class Destination(models.Model):
    TYPE_CHOICES = [
        ('beach', 'Beach'),
        ('hill', 'Hill'),
        ('forest', 'Forest'),
        ('historical', 'Historical'),
        ('lake', 'Lake'),
        ('city', 'City'),
    ]
    MONSOON_RISK_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('very_high', 'Very High'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_en = models.CharField(max_length=255)
    name_bn = models.CharField(max_length=255)
    division = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description_en = models.TextField()
    description_bn = models.TextField()
    best_months = models.JSONField(default=list)  # List of integers [10, 11, 12, 1, 2, 3]
    avoid_months = models.JSONField(default=list) # List of integers [6, 7, 8, 9]
    monsoon_risk = models.CharField(max_length=20, choices=MONSOON_RISK_CHOICES)
    flood_risk = models.BooleanField(default=False)
    road_access_monsoon = models.BooleanField(default=True)
    lat = models.FloatField()
    lng = models.FloatField()
    weather_city_id = models.CharField(max_length=100)
    images = models.JSONField(default=list)
    tags = models.JSONField(default=list)
    min_days_recommended = models.IntegerField(default=1)
    max_days_recommended = models.IntegerField(default=7)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_en

class Hotel(models.Model):
    PRICE_TIER_CHOICES = [
        ('budget', 'Budget'),
        ('midrange', 'Midrange'),
        ('premium', 'Premium'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    destination = models.ForeignKey(Destination, related_name='hotels', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    name_bn = models.CharField(max_length=255)
    star_rating = models.IntegerField(default=1)
    price_per_night_bdt = models.IntegerField()
    price_tier = models.CharField(max_length=20, choices=PRICE_TIER_CHOICES)
    amenities = models.JSONField(default=list)
    booking_url = models.URLField(max_length=500, null=True, blank=True)
    agoda_id = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.destination.name_en})"

class Restaurant(models.Model):
    PRICE_TIER_CHOICES = [
        ('budget', 'Budget'),
        ('midrange', 'Midrange'),
        ('premium', 'Premium'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    destination = models.ForeignKey(Destination, related_name='restaurants', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cuisine_type = models.CharField(max_length=100)
    avg_meal_cost_bdt = models.IntegerField()
    price_tier = models.CharField(max_length=20, choices=PRICE_TIER_CHOICES)
    google_place_id = models.CharField(max_length=255, null=True, blank=True)
    lat = models.FloatField()
    lng = models.FloatField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.destination.name_en})"

class Activity(models.Model):
    TYPE_CHOICES = [
        ('sightseeing', 'Sightseeing'),
        ('adventure', 'Adventure'),
        ('cultural', 'Cultural'),
        ('nature', 'Nature'),
        ('food', 'Food'),
    ]
    TIME_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('any', 'Any'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    destination = models.ForeignKey(Destination, related_name='activities', on_delete=models.CASCADE)
    name_en = models.CharField(max_length=255)
    name_bn = models.CharField(max_length=255)
    description_en = models.TextField()
    duration_hours = models.FloatField()
    cost_bdt = models.IntegerField(default=0)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    best_time_of_day = models.CharField(max_length=20, choices=TIME_CHOICES)
    is_monsoon_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name_en} ({self.destination.name_en})"

class TransportRoute(models.Model):
    MODE_CHOICES = [
        ('bus', 'Bus'),
        ('train', 'Train'),
        ('launch', 'Launch'),
        ('flight', 'Flight'),
        ('cng', 'CNG'),
        ('microbus', 'Microbus'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    origin_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    mode = models.CharField(max_length=20, choices=MODE_CHOICES)
    operator = models.CharField(max_length=255)
    avg_duration_minutes = models.IntegerField()
    avg_cost_bdt = models.IntegerField()
    booking_url = models.URLField(max_length=500, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.origin_city} to {self.destination_city} via {self.mode}"
