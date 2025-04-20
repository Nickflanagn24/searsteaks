"""Admin configuration for the bookings app.

This module registers models from the bookings app to make them accessible
in the Django admin interface, allowing administrators to manage user accounts,
restaurant tables, and customer reservations.
"""
from django.contrib import admin
from .models import CustomUser, Table, Booking

# Register models with the admin site
admin.site.register(CustomUser)
admin.site.register(Table)
admin.site.register(Booking)
