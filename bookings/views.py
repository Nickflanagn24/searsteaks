"""Views for handling restaurant booking system functionality."""
import logging
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
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
from datetime import datetime
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.views import generic
from django.db import IntegrityError

logger = logging.getLogger(__name__)

class CustomLoginView(LoginView):
    """Custom login view with restaurant-specific template."""
    template_name = 'bookings/login.html'

def register(request):
    """Handle user registration and account creation."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        # Debug POST data
        print("POST data received:", request.POST)
        
        if form.is_valid():
            print("Form is valid")
            user = form.save()
            login(request, user)
            print("User created and logged in:", user.username)
            messages.success(request, "Account created successfully! You are now logged in.")
            return redirect('home')
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Registration failed. Please check the form.")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'bookings/register.html', {'form': form})

def user_login(request):
    """Handle user authentication and login."""
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

def user_logout(request):
    """Log out the current user and redirect to home page."""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")

@login_required
@admin_required
def admin_dashboard(request):
    """Display admin dashboard for restaurant management."""
    return render(request, "bookings/admin_dashboard.html")

@login_required
@customer_required
def make_booking(request):
    """Handle creation of new table reservations."""
    table_id = request.GET.get('table_id')
    selected_date = request.GET.get('date')
    selected_time = request.GET.get('time')
    
    table = get_object_or_404(Table, id=table_id)
    
    if request.method == 'POST':
        guests = request.POST.get('guests')
        special_requests = request.POST.get('special_requests', '')
        
        if Booking.objects.filter(table=table, date=selected_date, time=selected_time).exists():
            messages.error(
                request, 
                f"Sorry, table {table.table_number} is already booked for this date and time. "
                "Please select another table or time slot."
            )
            return redirect('floor_plan')
        
        try:
            booking = Booking.objects.create(
                user=request.user,
                table=table,
                date=selected_date,
                time=selected_time,
                guests=guests,
                special_requests=special_requests
            )
            
            messages.success(request, "Your reservation has been confirmed!")
            return redirect('my_bookings')
            
        except IntegrityError:
            messages.error(request, "This table was just booked by someone else. Please try another table.")
            return redirect('floor_plan')
    
    return render(request, 'bookings/make_booking.html', {
        'table': table,
        'selected_date': selected_date,
        'selected_time': selected_time,
    })

def floor_plan(request):
    """Display restaurant floor plan with table availability."""
    selected_date = request.GET.get('date', datetime.now().strftime('%Y-%m-%d'))
    selected_time = request.GET.get('time', '18:30')
    
    tables = Table.objects.all()
    
    booked_table_ids = Booking.objects.filter(
        date=selected_date,
        time=selected_time
    ).values_list('table_id', flat=True)
    
    return render(request, 'bookings/floor_plan.html', {
        'tables': tables,
        'selected_date': selected_date,
        'selected_time': selected_time,
        'booked_table_ids': list(booked_table_ids),
        'today': datetime.now().strftime('%Y-%m-%d')
    })

@login_required
def my_bookings(request):
    """Show user's upcoming and past reservations."""
    all_bookings = Booking.objects.filter(user=request.user).order_by("date", "time")
    today = date.today()
    
    print(f"Found {len(all_bookings)} total bookings")
    
    upcoming_bookings = []
    past_bookings = []
    
    for booking in all_bookings:
        print(f"Booking: {booking.id}, Date: {booking.date}, Today: {today}")
        
        if booking.date >= today:
            upcoming_bookings.append(booking)
            print(f"Added to upcoming: {booking.id}")
        else:
            past_bookings.append(booking)
            print(f"Added to past: {booking.id}")
    
    print(f"Upcoming: {len(upcoming_bookings)}, Past: {len(past_bookings)}")
    
    return render(request, "bookings/my_bookings.html", {
        "upcoming_bookings": upcoming_bookings,
        "past_bookings": past_bookings,
        "today": today,
    })

@login_required
def delete_booking(request, booking_id):
    """Allow users to cancel their own reservations."""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking has been deleted from your history.")
        
    return redirect("my_bookings")

def home(request):
    """Render the restaurant's home page."""
    return render(request, "bookings/home.html")

def menu(request):
    """Display the restaurant's menu."""
    return render(request, "bookings/menu.html")

def contact(request):
    """Handle contact form submissions and inquiries."""
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message_text = request.POST.get('message', '')
        
        if not (first_name and last_name and email and subject and message_text):
            messages.error(request, "Please fill in all required fields.")
            return render(request, 'bookings/contact.html')
        
        formatted_message = f"""
        New Contact Form Submission
        --------------------------
        Name: {first_name} {last_name}
        Email: {email}
        Phone: {phone}
        Subject: {subject}
        
        Message:
        {message_text}
        """
        
        print("\n" + "="*50)
        print("NEW CONTACT FORM SUBMISSION")
        print("="*50)
        print(formatted_message)
        print("="*50 + "\n")
        
        try:
            send_mail(
                f"Contact Form: {subject}",
                formatted_message,
                email,
                ['prototype@searsteaks.com'],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Email sending failed: {e}")
        
        messages.success(request, "Thank you for your message! We'll get back to you soon.")
        return redirect('contact')
    
    return render(request, 'bookings/contact.html')

@login_required
@admin_required
def cancel_booking(request, booking_id):
    """Allow admins to cancel any reservation."""
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, "Booking successfully canceled.")
    return redirect("manage_bookings")

def table_availability(request):
    """API endpoint to get all tables with their availability."""
    date = request.GET.get('date')
    time = request.GET.get('time')
    
    if not date or not time:
        return JsonResponse({'error': 'Missing date or time parameter'}, status=400)
    
    tables = Table.objects.all()
    
    booked_table_ids = set(Booking.objects.filter(
        date=date,
        time=time
    ).values_list('table_id', flat=True))
    
    table_data = []
    for table in tables:
        table_data.append({
            'id': table.id,
            'table_number': table.table_number,
            'capacity': table.capacity,
            'is_booked': table.id in booked_table_ids
        })
    
    return JsonResponse({'tables': table_data})

def check_table_availability(request):
    """API endpoint to check if a specific table is available."""
    table_id = request.GET.get('table_id')
    date = request.GET.get('date')
    time = request.GET.get('time')
    
    if not all([table_id, date, time]):
        return JsonResponse({'error': 'Missing parameters'}, status=400)
    
    is_available = not Booking.objects.filter(
        table_id=table_id,
        date=date,
        time=time
    ).exists()
    
    return JsonResponse({'available': is_available})

# Add this new view for staff registration
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class StaffRegistrationView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'bookings/staff_register.html'
    success_url = reverse_lazy('admin_dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff_registration'] = True
        return context
    
    def form_valid(self, form):
        # Force role to be admin regardless of selection
        form.instance.role = 'admin'
        messages.success(self.request, "New staff member registered successfully!")
        return super().form_valid(form)

