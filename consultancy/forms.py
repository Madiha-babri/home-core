from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import consultancy


class consultancyForm(forms.ModelForm):
    """
    Form for creating and updating consultancy instances.

    **Fields**

        appointment_date: Date of the reservation.
        Design_type: Type of design to be selected
      

    **Labels**

        appointment_date: "Date"
        design_type: "Design"
        messages: "Messages"
    """

    class Meta:
        model = Booking
        fields = ("appointment_date", "design_type", "messages")
        widgets = {
            "appointment_date": DateInput(attrs={"type": "date"}),
        }

        labels = {
            "appointment_date": "Date",
            "design_type": "Design",
            "messages": "Messages",
        }