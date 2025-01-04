from django.shortcuts import render
from .models import Gallery

# Create your views here.
def home(request):
    gallery = Gallery.objects.all() 
    return render(request, 'gallery/gallery.html', {'gallery': gallery})