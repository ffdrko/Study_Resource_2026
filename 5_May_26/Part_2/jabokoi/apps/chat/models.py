from django.db import models
from django.conf import settings
import uuid

class Conversation(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('plan_generated', 'Plan Generated'),
        ('booked', 'Booked'),
        ('abandoned', 'Abandoned'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='conversations', on_delete=models.CASCADE)
    messages = models.JSONField(default=list)  # Array of {role: "user"|"assistant", content: "text"}
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Chat with {self.user.email} ({self.created_at})"

class TripPlan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, related_name='trip_plans', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='trip_plans', on_delete=models.CASCADE)
    destination = models.ForeignKey('destinations.Destination', on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    party_size = models.IntegerField()
    total_budget_bdt = models.IntegerField()
    hotel_budget_per_night_bdt = models.IntegerField()
    food_budget_per_day_bdt = models.IntegerField()
    plan_data = models.JSONField() # Full itinerary JSON
    is_edited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Plan for {self.destination.name_en if self.destination else 'Unknown'} ({self.start_date})"
