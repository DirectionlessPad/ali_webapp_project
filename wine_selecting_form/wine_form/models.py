from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# class User(AbstractUser):
#     pass

class Wine(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.CharField(max_length=500)