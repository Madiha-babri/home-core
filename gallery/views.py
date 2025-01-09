from django.shortcuts import render
from .models import Gallery


# Create your views here.
def home(request):
    """
    view to gallery designs
    """
    gallery = Gallery.objects.all() 
    return render(request, 'gallery/gallery.html', {'gallery': gallery})

# bedrooms options view
def bedrooms(request):
    """
    view to bedrooms design
    """
    return render(request, 'gallery/bedrooms.html')

# washroom options view
def washroom(request):
    """
    view to washroom designs
    """
    return render(request, 'gallery/washroom.html')

# kitchen options view
def kitchen(request):
    """
    view to kitchen designs
    """
    return render(request, 'gallery/kitchen.html')

# livingroom options view
def livingrooms(request):
    """
    view to livingrooms design
    """
    return render(request, 'gallery/livingrooms.html')
