from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Consultancy


@admin.register(Consultancy)
class ConsultancyAdmin(admin.ModelAdmin):
    """Class to view the consultancy in the admin panel"""

    list_display = (
        "username",
        "date_of_booking",
        "design_type",
        "message",
    )
    list_filter = ("date_of_booking", "username")
    search_fields = ["username", "design_type"]
    actions = ["confirm_consultancy"]

    def confirm_consultancy(self, request, queryset):
        queryset.update(confirmed=True)