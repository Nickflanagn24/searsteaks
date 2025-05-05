# bookings/templatetags/booking_extras.py
import time as time_module
from django import template

register = template.Library()


@register.filter
def time_to_seconds(value):
    """Convert a time string like '18:30' to seconds since midnight."""
    try:
        hours, minutes = map(int, value.split(':'))
        return hours * 3600 + minutes * 60
    except (ValueError, AttributeError):
        return 0


@register.filter
def subtract(value, arg):
    """Subtract the arg from the value."""
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return 0


@register.filter
def divide_by(value, arg):
    """Divide the value by the arg."""
    try:
        return int(value) / int(arg)
    except (ValueError, ZeroDivisionError, TypeError):
        return 0