from django.shortcuts import render,  get_object_or_404, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.utils.timezone import now
from django.contrib import messages
from django.urls import reverse_lazy     # for showing appointment confirmation
from django.http import HttpResponseRedirect

# booking view
    
@login_required
def book_appointment(request):
    template_name = "bookings/booking.html"
    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            bookings = booking_form.save(commit=False)
            bookings.owner = request.user
            bookings.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Booking submitted! It will turn from"
                + " colored to black when confirmed."
            )
            return HttpResponseRedirect(reverse("bookings"))
    else:
        booking_form = BookingForm()

    bookings = (
        Booking.objects.all()
        .filter(owner=request.user)
        .order_by("appointment_date")
    )

    return render(request, 
        "bookings/booking.html",
        {
            "bookings": bookings,
            "booking_form": booking_form,
        },
    )

# View to update the status of a booking
class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    template_name = "bookings/update_booking.html"
    form_class = BookingForm
    success_url = "/bookings/"

    def form_valid(self, form):
        form.instance.confirmed = False
        messages.success(
            self.request,
            "Your booking has been updated!",
            extra_tags="alert alert-success alert-dismissible",
        )

        return super().form_valid(form)

    def test_func(self):
        """
        Checks if the logged-in user is the owner of the booking.

        Returns:
            bool: True if the logged in user is the owner of the booking
            False otherwise.
        """
        booking = self.get_object()
        return (self.request.user == booking.owner or
                self.request.user.is_superuser)

# Appointment Cancellation View
class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    success_url = "/bookings/"

    def form_valid(self, form):
        messages.success(
            self.request,
            "Your booking has been deleted successfully!",
            extra_tags="alert alert-success alert-dismissible",
        )

        return super().form_valid(form)

    def test_func(self):
        """
        Checks if the logged-in user is the owner of the booking.

        Returns:
            bool: True if the logged in user is the owner of the booking
            False otherwise.
        """
        booking = self.get_object()
        return (self.request.user == booking.owner or
                self.request.user.is_superuser)

