from django.db import models
from django.contrib.auth.models import User
import datetime

DESIGNS = (("bedrooms", "Bedroom"), ("washroom", "Washroom"), ("kitchen", "Kitchen"), ("livigroom", "LivingRoom"))

# Create your models here.
class Consultancy(models.Model):

    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="username_booking"
    )
    date_of_booking = models.DateTimeField()
    design_type = models.TextField(choices=DESIGNS)
    confirmed = models.BooleanField(default=False)
    message = models.TextField(max_length=500)

    class Meta:
        ordering = ["date_of_booking"]

    def __str__(self):
        return (
            f"Booking for {self.username} on {self.date_of_booking}"
        )
