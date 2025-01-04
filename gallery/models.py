from django.db import models

# Create your models here.
class Gallery(models.Model):
    """
    Stores a single gallery text
    """
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

