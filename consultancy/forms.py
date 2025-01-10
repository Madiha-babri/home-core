from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Consultancy


class ConsultancyForm(forms.ModelForm):
    """
    Form for creating and updating consultancy instances.

    **Fields**

        date_of_booking: Date of the reservation.
        Design_type: Type of design to be selected
      

    **Labels**

        date_of_booking: "Date"
        design_type: "Design"
        message: "Message"
    """

    class Meta:
        model = Consultancy
        fields = ("date_of_booking", "design_type", "message")
        widgets = {
            "date_of_booking": DateInput(attrs={"type": "date"}),
        }

        labels = {
            "date_of_booking": "Date",
            "design_type": "Design",
            "message": "Message",
        }