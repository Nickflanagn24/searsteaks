from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .decorators import role_required, customer_required
from .models import Table

# Register View
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        else:
            messages.error(request, "Registration failed. Please check the form.")
    else:
        form = CustomUserCreationForm()
    return render(request, "bookings/register.html", {"form": form})

# Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "bookings/login.html", {"form": form})

# Logout View
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

# Admin Dashboard View
@login_required
@role_required('admin')
def admin_dashboard(request):
    return render(request, "bookings/admin_dashboard.html")

# Booking Views
@login_required
@customer_required
def make_booking(request):
    return render(request, "bookings/make_booking.html")

@login_required
@customer_required
def my_bookings(request):
    return render(request, "bookings/my_bookings.html")

# Floor Plan View
def floor_plan(request):
    tables = Table.objects.all()  # Fetch all tables from the database
    return render(request, "bookings/floor_plan.html", {"tables": tables})

