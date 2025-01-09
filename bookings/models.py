from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    username = models.CharField(max_length=255, default="default_user")
    date_of_booking = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=255)
    design_style = models.CharField(max_length=100, blank=True)    # user can choose any design for booking
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    notes = models.TextField(blank=True)                           # user can enter additional notes

    def __str__(self):
        return f"Booking for {self.username} on {self.date_of_booking}"

    class Meta:
        ordering = ["date_of_booking"]