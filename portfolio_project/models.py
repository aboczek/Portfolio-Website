from django.db import models

# Create your models here.

class Details(models.Model):
    """
    Database model for details.
    """
    full_name = models.CharField(max_length=50)
    age = models.PositiveBigIntegerField()
    nationality = models.CharField(max_length=50)
    languages = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
