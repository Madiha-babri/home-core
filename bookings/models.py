from django.db import models
from django.contrib.auth.models import User
import datetime

DESIGNS = (("bedrooms", "Bedroom"), ("washroom", "Washroom"), ("kitchen", "Kitchen"), ("livigroom", "LivingRoom"))

class Booking(models.Model):
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
