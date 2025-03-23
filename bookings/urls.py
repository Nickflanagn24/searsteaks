from django.urls import path, include
from . import views
from django.contrib import admin
from .views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('make-booking/', views.make_booking, name='make_booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('floor-plan/', views.floor_plan, name='floor_plan'),
    path('admin/cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's built-in auth URLs
]
