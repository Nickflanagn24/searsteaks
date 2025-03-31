from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, BookingForm
from .decorators import admin_required, customer_required
from .models import Table, Booking
from django.contrib.auth.views import LoginView
from datetime import date

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
    table_id = request.GET.get('table_id')  # Get the table ID from the query parameters
    selected_date = request.GET.get('date')  # Get the selected date from the query parameters
    selected_time = request.GET.get('time')  # Get the selected time slot from the query parameters

    # Fetch the table object
    table = get_object_or_404(Table, id=table_id)

    if request.method == "POST":
        guests = request.POST.get('guests')  # Get the number of guests from the form
        Booking.objects.create(
            user=request.user,
            table=table,
            date=selected_date,
            time=selected_time,
            guests=guests  # Use the value provided by the user
        )
        return redirect("my_bookings")  # Redirect to the user's bookings page

    # Render the booking details page
    return render(request, "bookings/make_booking.html", {
        "table": table,
        "selected_date": selected_date,
        "selected_time": selected_time,
    })

def floor_plan(request):
    tables = Table.objects.all()
    today = date.today().strftime("%Y-%m-%d")  # Format as "YYYY-MM-DD"
    for table in tables:
        # Example logic to determine availability
        bookings = Booking.objects.filter(table=table, date=today)
        table.is_available = not bookings.exists()  # Table is available if no bookings exist for today
    return render(request, 'bookings/floor_plan.html', {'tables': tables, 'today': today})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by("date", "time")
    return render(request, "bookings/my_bookings.html", {"bookings": bookings})

def home(request):
    return render(request, "bookings/home.html")

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

