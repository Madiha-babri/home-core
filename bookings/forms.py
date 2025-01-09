from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from datetime import datetime, date
from .models import Booking
from django.forms import ModelForm

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['date_of_booking', 'location', 'design_style', 'status', 'notes']

    date_of_booking = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))