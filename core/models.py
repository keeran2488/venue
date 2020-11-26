from django.db import models
from django.contrib.auth.models import User


class VenueDetails(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=255)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to = 'profile/')
