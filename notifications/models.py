from django.db import models

from authentication.models import User


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=15)
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
