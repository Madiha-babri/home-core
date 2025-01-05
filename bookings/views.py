from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Booking
from .forms import BookingForm

# Create your views here.
class CreateBookingView(CreateView):
    model = Booking
    template_name = "bookings/booking.html"
    fields = ['user', 'date', 'location', 'design_style', 'notes']


def create_booking(request):
    template_name = "bookings/create_booking.html"
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/create_booking.html', {'form': form})


# View to list all bookings
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

# View to update the status of a booking
def update_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        booking.status = request.POST.get('status')
        booking.save()
        return redirect('booking_list')
    return render(request, 'bookings/update_booking.html', {'booking': booking})