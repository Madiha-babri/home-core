from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):

    """
    A form for creating collaboration requests
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')