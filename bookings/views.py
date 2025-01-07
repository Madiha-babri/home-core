from django.shortcuts import render,  get_object_or_404, redirect
from django.views.generic.edit import CreateView
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib import messages
from django.urls import reverse_lazy     # for showing appointment confirmation

# Create your views here.
class CreateBookingView(CreateView):
    model = Booking
    template_name = "bookings/booking.html"
    fields = ['user', 'date', 'location', 'design_style', 'notes']
    success_url = reverse_lazy('appointment_confirmation')

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


# Appointment Cancellation View
@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Check if the user is either the patient or the specialist linked to the appointment
    if request.method == 'POST':
        if request.user == appointment.patient.user or request.user == appointment.specialist.user:
            appointment.status = 'Cancelled'
            appointment.save()
            messages.success(request, 'The appointment has been successfully canceled.')
        else:
            messages.error(request, 'You do not have permission to cancel this appointment.')

        # Redirect based on user type (patient or specialist)
        if request.user.groups.filter(name='Patient').exists():
            return redirect('patient_appointments')
        elif request.user.groups.filter(name='Specialist').exists():
            return redirect('specialist_appointments')

        return redirect('home')

    # Render the confirmation page if it's not a POST request
    return render(request, 'appointments/confirm_cancellation.html', {'appointment': appointment})


# Appointment Cancellation Confirmation View
@login_required
def confirm_cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Check if the user is either the patient or the specialist linked to the appointment
    if request.user == appointment.patient.user or request.user == appointment.specialist.user:
        if request.method == 'POST':  # User confirmed the cancellation
            appointment.status = 'Cancelled'
            appointment.save()
            messages.success(request, 'The appointment has been successfully canceled.')
            
            # Redirect based on user type (patient or specialist)
            if request.user.groups.filter(name='Patient').exists():
                return redirect('patient_appointments')
            elif request.user.groups.filter(name='Specialist').exists():
                return redirect('specialist_appointments')
        else:  # GET request, show confirmation page
            is_patient = request.user.groups.filter(name='Patient').exists()
            return render(request, 'appointments/confirm_cancellation.html', {
                'appointment': appointment,
                'is_patient': is_patient,
            })
    else:
        messages.error(request, 'You do not have permission to cancel this appointment.')
        return redirect('home')

def bedrooms(request):
    return render(request, 'bookings/bedrooms.html')
