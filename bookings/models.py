from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Custom User Model for Authentication
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')

# Table Model - Represents restaurant tables
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} ({self.capacity} seats)"

# Booking Model - Stores customer reservations
class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=10)  # e.g., "18:30" or "21:30"
    guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        # Validate time slot
        valid_times = ['18:30', '21:30']
        if self.time not in valid_times:
            raise ValidationError({'time': 'Invalid time slot selected.'})
    
    def __str__(self):
        return f"Booking for {self.user} on {self.date} at {self.time}"
