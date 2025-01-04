from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'date', 'address', 'design_style', 'notes']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }