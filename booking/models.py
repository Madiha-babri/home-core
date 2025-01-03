from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Consultant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=100)  # Type of expertise (e.g., Interior Designer, Color Consultant, etc.)
    bio = models.TextField()
    rating = models.FloatField(default=0.0)  # Rating for the consultant

    def __str__(self):
        return self.user.username

# Define Booking model
class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The customer booking the consultation
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)  # The assigned consultant
    consultation_date = models.DateTimeField()  # The date and time of the consultation
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')  # Booking status
    notes = models.TextField(blank=True, null=True)  # Optional field for special requests or notes
    created_at = models.DateTimeField(auto_now_add=True)  # When the booking was created

    def __str__(self):
        return f"Booking with {self.consultant.user.username} for {self.user.username} on {self.consultation_date}"

    class Meta:
        ordering = ['-created_at']  # Order bookings by creation time (latest first)