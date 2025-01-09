from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Class to view the Bookings in the admin panel"""

    list_display = (
        "username",
        "email",
        "appointment_date",
        "design_style",
        "notes",
    )
    list_filter = ("appointment_date", "username")
    search_fields = ["username", "design_style"]
    actions = ["confirm_booking"]

    def confirm_booking(self, request, queryset):
        queryset.update(confirmed=True)