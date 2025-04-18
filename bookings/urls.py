from django.urls import path, include
from django.contrib.auth.views import LoginView  # Add this import
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('make-booking/', views.make_booking, name='make_booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('floor-plan/', views.floor_plan, name='floor_plan'),
    path('test-floor-plan/', views.test_floor_plan, name='test_floor_plan'),
    path('api/table-availability/', views.table_availability, name='table_availability'),
    path('admin/cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('internal/staff-registration/', views.StaffRegistrationView.as_view(), name='staff_register'),
    path('api/check-availability/', views.check_table_availability, name='check_availability'),
]
