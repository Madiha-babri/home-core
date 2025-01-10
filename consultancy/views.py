from django.shortcuts import render,  get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.utils.timezone import now
from django.contrib import messages
from django.urls import reverse_lazy     # for showing appointment confirmation
from .models import consultancy
from .forms import ConsultancyForm

@login_required
def book_consultancy(request):
    """
    Renders the consultancy page with booking functionality

    **Context**

     ``consultancy``
        All bookings made by the current user, ordered by date
        from :model:`consultancy.Consultancy`
    ``consultancy_form``
        An instance of :form:`bookings.BookingForm` for submitting
        booking requests.

     **Template**
        :template:`consultancy/consultancy.html`
    """
    template_name = "consultancy/consultancy.html"
    if request.method == 'POST':
        consultancy_form = ConsultancyForm(data=request.POST)
        if consultancy_form.is_valid():
            consultancy = consultancy_form.save(commit=False)
            consultancy.username = request.user
            consultancy.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "consultancy Booking Received! It will turn from"
                + " colored to black when confirmed."
            )
            return HttpResponseRedirect(reverse("consultancy"))
    else:
        consultancy_form = ConsultancyForm()

    consultancy = (
        Consultancy.objects.all()
        .filter(username=request.user)
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
    """
    Edit a booking

    Uses :model: `booking.Booking`

    **Context**

    ``booking``
        represents the booking instance to be edited

     **Template**

    :template:`bookings/update_booking.html`

    """
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
        return (self.request.user == booking.username or
                self.request.user.is_superuser)

# Appointment Cancellation View
class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Displays a new page to confirm deletion of a booking

    Uses :model: `booking.Booking`

    **Context**

    ``booking``
        Represents the booking instance to be deleted.
        Comes from :model:`bookings.Booking`

    **Template**

    :template:`bookings/confirm_delete.html`

    Redirects to success url which is "/bookings/"
    """
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
        return (self.request.user == booking.username or
                self.request.user.is_superuser)
