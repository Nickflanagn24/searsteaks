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
    template_name = 'bookings/login.html'

# Simplified registration view for debugging
def register(request):
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
            return redirect('home')  # Make sure this URL name exists
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Registration failed. Please check the form.")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'bookings/register.html', {'form': form})

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
    table_id = request.GET.get('table_id')
    selected_date = request.GET.get('date')
    selected_time = request.GET.get('time')
    
    # Get the table
    table = get_object_or_404(Table, id=table_id)
    
    if request.method == 'POST':
        guests = request.POST.get('guests')
        special_requests = request.POST.get('special_requests', '')
        
        # Check if table is already booked
        if Booking.objects.filter(table=table, date=selected_date, time=selected_time).exists():
            messages.error(
                request, 
                f"Sorry, table {table.table_number} is already booked for this date and time. "
                "Please select another table or time slot."
            )
            return redirect('floor_plan')
        
        try:
            # Create the booking
            booking = Booking.objects.create(
                user=request.user,
                table=table,
                date=selected_date,
                time=selected_time,
                guests=guests,
                special_requests=special_requests
            )
            
            # Show a success message
            messages.success(request, "Your reservation has been confirmed!")
            
            # Redirect to the my_bookings page
            return redirect('my_bookings')
            
        except IntegrityError:
            # This is a fallback in case two requests try to book 
            # the same table simultaneously
            messages.error(request, "This table was just booked by someone else. Please try another table.")
            return redirect('floor_plan')
    
    # For GET requests, render the booking form
    return render(request, 'bookings/make_booking.html', {
        'table': table,
        'selected_date': selected_date,
        'selected_time': selected_time,
    })

def floor_plan(request):
    # Get date and time parameters or use defaults
    selected_date = request.GET.get('date', datetime.now().strftime('%Y-%m-%d'))
    selected_time = request.GET.get('time', '18:30')  # Default to 6:30 PM
    
    # Get all tables
    tables = Table.objects.all()
    
    # Get all bookings for the selected date and time
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
    # Get all bookings for the current user
    all_bookings = Booking.objects.filter(user=request.user).order_by("date", "time")
    today = date.today()
    
    # Print debugging info to console
    print(f"Found {len(all_bookings)} total bookings")
    
    # Separate bookings into upcoming and past
    upcoming_bookings = []
    past_bookings = []
    
    for booking in all_bookings:
        # Print each booking for debugging
        print(f"Booking: {booking.id}, Date: {booking.date}, Today: {today}")
        
        # Compare booking date with today's date
        if booking.date >= today:
            upcoming_bookings.append(booking)
            print(f"Added to upcoming: {booking.id}")
        else:
            past_bookings.append(booking)
            print(f"Added to past: {booking.id}")
    
    # Print final counts
    print(f"Upcoming: {len(upcoming_bookings)}, Past: {len(past_bookings)}")
    
    return render(request, "bookings/my_bookings.html", {
        "upcoming_bookings": upcoming_bookings,
        "past_bookings": past_bookings,
        "today": today,
    })

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == "POST":
        # Delete the booking
        booking.delete()
        messages.success(request, "Booking has been deleted from your history.")
        
    return redirect("my_bookings")

def home(request):
    return render(request, "bookings/home.html")

def menu(request):
    return render(request, "bookings/menu.html")

def contact(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message_text = request.POST.get('message', '')
        
        # Simple validation
        if not (first_name and last_name and email and subject and message_text):
            messages.error(request, "Please fill in all required fields.")
            return render(request, 'bookings/contact.html')
        
        # Format the message
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
        
        # For prototyping, we'll print to console instead of sending email
        print("\n" + "="*50)
        print("NEW CONTACT FORM SUBMISSION")
        print("="*50)
        print(formatted_message)
        print("="*50 + "\n")
        
        try:
            # Try to send email, but don't fail if it doesn't work
            send_mail(
                f"Contact Form: {subject}",
                formatted_message,
                email,  # From address (the user's email)
                ['prototype@searsteaks.com'],  # To address
                fail_silently=True,  # Changed to True so it doesn't raise exceptions
            )
        except Exception as e:
            # Log the exception but don't stop execution
            print(f"Email sending failed: {e}")
            # The message is already printed to console above
        
        # Show success message
        messages.success(request, "Thank you for your message! We'll get back to you soon.")
        return redirect('contact')
    
    return render(request, 'bookings/contact.html')

@login_required
@admin_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, "Booking successfully canceled.")
    return redirect("manage_bookings")

def table_availability(request):
    date = request.GET.get('date')
    time = request.GET.get('time')
    
    if not date or not time:
        return JsonResponse({'error': 'Missing date or time parameter'}, status=400)
    
    # Get all tables
    tables = Table.objects.all()
    
    # Get all bookings for the selected date and time
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

def test_floor_plan(request):
    """A simple self-contained test view to diagnose rendering issues."""
    
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Test Floor Plan</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            .table-card {
                border: 2px solid #ddd;
                border-radius: 8px;
                padding: 15px;
                margin: 10px;
                text-align: center;
                display: inline-block;
                width: 200px;
            }
            .available {
                background-color: rgba(139, 195, 74, 0.1);
                border-color: #8bc34a;
            }
            .booked {
                background-color: rgba(244, 67, 54, 0.1);
                border-color: #f44336;
            }
            .status-available { color: green; }
            .status-booked { color: red; }
            .table-number { font-weight: bold; font-size: 18px; }
        </style>
    </head>
    <body>
        <div class="container mt-4">
            <h1 class="text-center">Test Floor Plan</h1>
            
            <div class="row mb-4">
                <div class="col-md-12">
                    <div class="card">
                        <div class="card-header bg-dark text-white">
                            <h3>Select Date & Time</h3>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-md-5">
                                    <label for="date">Date:</label>
                                    <input type="date" id="date" class="form-control" value="2025-04-06">
                                </div>
                                <div class="col-md-5">
                                    <label for="time">Time:</label>
                                    <select id="time" class="form-control">
                                        <option value="18:30">6:30 PM</option>
                                        <option value="21:30">9:30 PM</option>
                                    </select>
                                </div>
                                <div class="col-md-2">
                                    <label>&nbsp;</label>
                                    <button id="check-btn" class="btn btn-primary form-control">Check</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="row">
                <div class="col-md-12">
                    <div class="card">
                        <div class="card-header bg-dark text-white">
                            <h3>Available Tables</h3>
                        </div>
                        <div class="card-body text-center" id="tables-container">
                            <p>Please select a date and time to view tables.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                const checkBtn = document.getElementById('check-btn');
                const tablesContainer = document.getElementById('tables-container');
                
                // Sample table data
                const tables = [
                    {id: 1, number: 1, capacity: 2},
                    {id: 2, number: 2, capacity: 4},
                    {id: 3, number: 3, capacity: 2}, 
                    {id: 4, number: 4, capacity: 6},
                    {id: 5, number: 5, capacity: 4},
                    {id: 6, number: 6, capacity: 2},
                    {id: 7, number: 7, capacity: 4},
                    {id: 8, number: 8, capacity: 8}
                ];
                
                checkBtn.addEventListener('click', function() {
                    // Clear container
                    tablesContainer.innerHTML = '<div>Loading tables...</div>';
                    
                    // Get date and time
                    const date = document.getElementById('date').value;
                    const time = document.getElementById('time').value;
                    
                    // Small delay to simulate loading (not needed in production)
                    setTimeout(function() {
                        // Clear container again
                        tablesContainer.innerHTML = '';
                        
                        // Add tables
                        tables.forEach(table => {
                            // Random availability (for demo)
                            const available = Math.random() > 0.3;
                            
                            // Create table card
                            const tableCard = document.createElement('div');
                            tableCard.className = `table-card ${available ? 'available' : 'booked'}`;
                            
                            tableCard.innerHTML = `
                                <div class="table-number">Table ${table.number}</div>
                                <div>Capacity: ${table.capacity}</div>
                                <div class="status-${available ? 'available' : 'booked'}">
                                    ${available ? 'Available' : 'Booked'}
                                </div>
                                ${available ? '<button class="btn btn-sm btn-success mt-2">Book</button>' : ''}
                            `;
                            
                            tablesContainer.appendChild(tableCard);
                        });
                    }, 500);
                });
            });
        </script>
        
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    
    return HttpResponse(html)

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

