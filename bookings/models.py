"""Models for user authentication and restaurant booking system."""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    """Extended user model with restaurant-specific fields."""
    phone_number = models.CharField(max_length=15, blank=True)
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='customer')


class Table(models.Model):
    """Restaurant table with number, capacity and availability status."""
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} ({self.capacity} seats)"


class Booking(models.Model):
    """Reservation record linking users to tables at specific dates and times."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=10)  # e.g., "18:30" or "21:30"
    guests = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta options for the Booking model."""
        constraints = [
            models.UniqueConstraint(
                fields=['table', 'date', 'time'],
                name='unique_booking'
            )
        ]

    def clean(self):
        """Validate time slots and check for double bookings."""
        # Validate time slot
        valid_times = ['18:30', '21:30']
        if self.time not in valid_times:
            raise ValidationError({'time': 'Invalid time slot selected.'})

        # Check for existing bookings
        if Booking.objects.filter(
                table=self.table,
                date=self.date,
                time=self.time).exists():
            raise ValidationError(
                'This table is already booked for the selected time.')

    def __str__(self):
        return f"Booking for {self.user} on {self.date} at {self.time}"


class ContactMessage(models.Model):
    """Model for storing contact form submissions."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        """Meta options for the ContactMessage model."""
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.subject} - {self.first_name} {self.last_name}"