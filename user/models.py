from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)

    hasShop = models.BooleanField(default=False, blank=True)