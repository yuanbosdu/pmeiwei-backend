from django.db import models
from django.conf import settings
import os

# Create your models here.

from django.contrib.auth.models import AbstractUser


def user_upload_to(instance, filename):
    return os.path.join(instance.username, filename)


class User(AbstractUser):

    avatar = models.ImageField(upload_to=user_upload_to, blank=True, null=True)

    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)

    hasShop = models.BooleanField(default=False, blank=True)