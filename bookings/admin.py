from django.contrib import admin
from .models import Booking

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['username', 'date_of_booking', 'address', 'design_style', 'status']
    list_filter = ['status', 'username', 'date_of_booking']
    search_fields = ['username', 'location']
    actions = ["confirm_booking"]

    def confirm_booking(self, request, queryset):
        queryset.update(confirmed=True)