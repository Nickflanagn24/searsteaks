"""Admin configuration for the bookings app.

This module registers models from the bookings app to make them accessible
in the Django admin interface, allowing administrators to manage user accounts,
restaurant tables, and customer reservations.
"""
from django.contrib import admin
from .models import CustomUser, Table, Booking, ContactMessage

# Register models with the admin site
admin.site.register(CustomUser)
admin.site.register(Table)
admin.site.register(Booking)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'first_name', 'last_name',
                    'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'subject', 'message')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected messages as unread"

    actions = [mark_as_read, mark_as_unread]
