from django.contrib import admin
from .models import CustomUser, Table, Booking

admin.site.register(CustomUser)
admin.site.register(Table)
admin.site.register(Booking)
