from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    preferred_language = models.CharField(max_length=5, choices=[('bn', 'Bengali'), ('en', 'English')], default='en')
    is_nrb = models.BooleanField(default=False)
    country_of_residence = models.CharField(max_length=100, null=True, blank=True)
    currency_preference = models.CharField(max_length=5, choices=[('BDT', 'Bangladeshi Taka'), ('USD', 'US Dollar')], default='BDT')
    created_at = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
