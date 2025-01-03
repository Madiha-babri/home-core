from django.shortcuts import render
from .models import Gallery

# Create your views here.
def home(request):
    rooms = Room.objects.all()  # Get all rooms
    return render(request, 'gallery/gallery.html', {'gallery': gallery})