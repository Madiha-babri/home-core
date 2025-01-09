from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gallery(models.Model):
    """
    Stores a single gallery design text
    """
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

