from django.db import models
from django.contrib.auth.models import User
import datetime

class Booking(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owner_booking")
    email = models.EmailField()
    appointment_date = models.DateTimeField()
    design_style = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed')], default='pending')
    
    def __str__(self):
        return f'Booking for {self.owner} on {self.appointment_date}'

    class Meta:
        ordering = ['appointment_date']

