from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("make-booking/", views.make_booking, name="make_booking"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path("floor-plan/", views.floor_plan, name="floor_plan"),
]
