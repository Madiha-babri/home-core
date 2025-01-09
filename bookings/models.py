from django.db import models
from django.contrib.auth.models import User
import datetime

DESIGNS = (("bedrooms", "Bedroom"), ("washroom", "Washroom"), ("kitchen", "Kitchen"), ("livigroom", "LivingRoom"))

class Booking(models.Model):
    """
    Model for bookings with username related to :model:`auth.User`.

    Fields:
        - `username` (ForeignKey): Reference to the user making the booking.
        - `appointment_date` (DateField): Date of the reservation.
        - `design_style` (IntegerField): Reference to the design.
        - `confirmed` (BooleanField): Indicates whether the booking is
        confirmed.
        - `notes` (CharField): A free text area to allow the customer to
        make addition comments or ask a question.

    Meta:
        - `ordering`: Default ordering for queries based on date.

    Methods:
        - `__str__`: Human-readable string representation of the booking.
    """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="username_booking")
    email = models.EmailField()
    appointment_date = models.DateTimeField()
    design_style = models.TextField(choices=DESIGNS)
    notes = models.TextField(default="No notes provided")
    confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Booking for {self.username} on {self.appointment_date}'

    class Meta:
        ordering = ['appointment_date']
