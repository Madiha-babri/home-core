from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from datetime import datetime, date
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Form for creating and updating booking instances.

    **Fields**

        appointment_date: Date of the reservation.
        Design_style: Type of design to be selected
      

    **Labels**

        appointment_date: "Date"
        design_style: "Design"
        email: "Email"
    """

    class Meta:
        model = Booking
        fields = ("appointment_date", "design_style", "email", "notes")
        widgets = {
            "appointment_date": DateInput(attrs={"type": "date"}),
        }

        labels = {
            "appointment_date": "Date",
            "design_style": "Design",
            "email": "Email",
            "notes": "Notes",
        }
