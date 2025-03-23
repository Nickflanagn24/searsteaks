from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, BookingForm
from .decorators import admin_required, customer_required
from .models import Table, Booking
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'bookings/login.html'

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
    return redirect("home")  # Redirect to home page after logging out

# Admin Dashboard View
@login_required
@admin_required
def admin_dashboard(request):
    return render(request, "bookings/admin_dashboard.html")

# Booking Views
@login_required
@customer_required
def make_booking(request):
    table_id = request.GET.get("table_id")  # Get table from URL
    table = get_object_or_404(Table, id=table_id) if table_id else None

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, "Booking successful!")
            return redirect("my_bookings")  # Redirect to booking list page
    else:
        form = BookingForm(initial={"table": table})

    return render(request, "bookings/make_booking.html", {"form": form, "table": table})

def floor_plan(request):
    tables = Table.objects.all()  # Fetch all tables from the database
    return render(request, "bookings/floor_plan.html", {"tables": tables})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by("date", "time")
    return render(request, "bookings/my_bookings.html", {"bookings": bookings})

def home(request):
    return render(request, "bookings/index.html")

def menu(request):
    return render(request, "bookings/menu.html")

def contact(request):
    return render(request, "bookings/contact.html")

@login_required
@admin_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, "Booking successfully canceled.")
    return redirect("manage_bookings")

