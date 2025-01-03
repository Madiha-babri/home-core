from django.contrib import admin
from .models import Booking, Consultant

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'consultant', 'consultation_date', 'status', 'created_at')
    list_filter = ('status', 'consultant')
    search_fields = ('user__username', 'consultant__user__username')

admin.site.register(Booking, BookingAdmin)
admin.site.register(Consultant)