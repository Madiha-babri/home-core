from django.db import models
from django.contrib.auth.models import User
import datetime

DESIGNS = (("bedrooms", "Bedroom"), ("washroom", "Washroom"), ("kitchen", "Kitchen"), ("livigroom", "LivingRoom"))

class Booking(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owner_booking")
    email = models.EmailField()
    appointment_date = models.DateTimeField()
    design_style = models.TextField(choices=DESIGNS)
    confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Booking for {self.owner} on {self.appointment_date}'

    class Meta:
        ordering = ['appointment_date']

