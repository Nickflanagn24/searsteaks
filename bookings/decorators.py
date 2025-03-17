from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def admin_required(view_func):
    """Decorator to restrict access to admin users only."""
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "admin":
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You do not have permission to view this page.")
    return wrapper

def customer_required(view_func):
    """Decorator to restrict access to customers only."""
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == "customer":
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You do not have permission to access this page.")
    return wrapper
