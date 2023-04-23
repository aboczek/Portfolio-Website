from django.db import models
from cloudinary.models import CloudinaryField

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
        return str(self.full_name)


class Skills(models.Model):
    """
    Database model for skills.
    """
    skill = models.CharField(max_length=200)

    def __str__(self):
        return str(self.skill)


class Projects(models.Model):
    """
    Database model for projects.
    """

    title = models.CharField(max_length=200)
    project_link = models.URLField(max_length=250)
    project_description = models.TextField()
    project_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return str(self.title)
