from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import consultancy

@admin.register(Consultancy)
class consultancyAdmin(admin.ModelAdmin):
    """Class to view the consultancy in the admin panel"""

    list_display = (
        "username",
        "appointment_date",
        "design_type",
        "message",
    )
    list_filter = ("appointment_date", "username")
    search_fields = ["username", "design_type"]
    actions = ["confirm_consultancy"]

    def confirm_consultancy(self, request, queryset):
        queryset.update(confirmed=True)
