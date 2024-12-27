from django.db import models

# Create your models here.
class About(models.Model):
    """
    Stores a single about me text
    """

    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ["updated_on"]

    def __str__(self):
        return self.title