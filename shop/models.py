from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Shop(models.Model):
    """
    Stores a single about me text
    """

    title = models.CharField(max_length=200)
    profile_image = CloudinaryField("image", default="placeholder")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ["updated_on"]

    def __str__(self):
        return self.title