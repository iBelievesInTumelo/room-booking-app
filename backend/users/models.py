from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Table for users overidding default user provided by Django, some fields need
     tweeking to circumvent default behaviour """
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) :
        return f'{self.name}'

class Room(models.Model):
    """ Table for storing rooms """
    title = models.CharField(max_length=128)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.URLField(max_length=200)


class Bookings(models.Model):
    """ Table for storing bookings """
    booking_start = models.DateField()
    booking_end  = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)

