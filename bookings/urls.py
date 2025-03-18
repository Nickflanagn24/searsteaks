from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Home page
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("make-booking/", views.make_booking, name="make_booking"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path("floor-plan/", views.floor_plan, name="floor_plan"),
]

# URL pattern for the cancellation route
urlpatterns += [
    path("admin/cancel-booking/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
]
