"""ASGI configuration for restaurant_booking project."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant_booking.settings")

application = get_asgi_application()
