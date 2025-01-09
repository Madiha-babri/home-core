from django.shortcuts import render
from .models import Gallery


# Create your views here.
def home(request):
    gallery = Gallery.objects.all() 
    return render(request, 'gallery/gallery.html', {'gallery': gallery})

# bedrooms options view
def bedrooms(request):
    return render(request, 'gallery/bedrooms.html')

# washroom options view
def washroom(request):
    return render(request, 'gallery/washroom.html')

# kitchen options view
def kitchen(request):
    return render(request, 'gallery/kitchen.html')

# livingroom options view
def livingrooms(request):
    return render(request, 'gallery/livingrooms.html')
