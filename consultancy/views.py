from django.shortcuts import render,  get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.utils.timezone import now
from django.contrib import messages
from django.urls import reverse     # for showing appointment confirmation
from .models import Consultancy
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
        .order_by("date_of_booking")
    )

    return render(request, 
        "consultancy/consultancy.html",
        {
            "consultancy": consultancy,
            "consultancy_form": consultancy_form,
        },
    )
