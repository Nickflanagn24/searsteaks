"""Configuration for the bookings app."""
from django.apps import AppConfig


class BookingsConfig(AppConfig):
    """Configuration class for the restaurant booking application."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'
