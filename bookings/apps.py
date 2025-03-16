from django.contrib.auth.models import AbstractUser
from django.db import models

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
        return f"Table {self.table_number} - Capacity: {self.capacity}"

# Booking Model - Stores customer reservations
class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"Booking by {self.user.username} on {self.date} at {self.time}"
