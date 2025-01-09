from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Class to view the Bookings in the admin panel"""

    list_display = (
        "owner",
        "email",
        "appointment_date",
        "design_style",
    )
    list_filter = ("appointment_date", "owner")
    search_fields = ["owner", "design_style"]
    actions = ["confirm_booking"]

    def confirm_booking(self, request, queryset):
        queryset.update(confirmed=True)