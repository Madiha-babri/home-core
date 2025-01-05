from django.contrib import admin
from .models import Booking

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'location', 'status']
    list_filter = ['status', 'date']
    search_fields = ['user__username', 'address']
    ordering = ['date']

admin.site.register(Booking, BookingAdmin)