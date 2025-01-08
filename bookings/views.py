from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic.edit import CreateView
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import now
from django.contrib import messages
from django.urls import reverse_lazy     # for showing appointment confirmation


# booking view

class CreateBookingView(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = "bookings/booking.html"
    fields = ['user', 'date', 'location', 'design_style', 'notes']
    success_url = reverse_lazy('booking_list')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
@login_required
def book_appointment(request):
    template_name = "bookings/booking.html"
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            appointment.status = 'Pending'  # Set the default status to 'Pending'
            booking.save()
            return redirect('booking_confirmation')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking.html', {'form': form})

 # Confirmation view
def booking_confirmation(request):
    return render(request, 'bookings/booking_confirmation.html')


# View to list all bookings
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

# View to update the status of a booking
def user_can_modify_booking(user, booking):
    if booking.user != user:
        raise PermissionDenied
        
def update_booking(request, pk):

    queryset = Post.objects.filter(user=request.user)
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'update_booking.html', {'form': form})

# Appointment Cancellation View
def delete_booking(request, pk):

    queryset = Post.objects.filter(user=request.user)
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'confirm_delete.html', {'booking': booking})


# bedrooms options view
def bedrooms(request):
    return render(request, 'bookings/bedrooms.html')

# washroom options view
def washroom(request):
    return render(request, 'bookings/washroom.html')

# kitchen options view
def kitchen(request):
    return render(request, 'bookings/kitchen.html')

# livingroom options view
def livingrooms(request):
    return render(request, 'bookings/livingrooms.html')

