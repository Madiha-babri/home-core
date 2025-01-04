from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    address = models.CharField(max_length=255)
    design_style = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Booking for {self.user.username} on {self.date}"
