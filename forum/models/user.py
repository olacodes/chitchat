from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import Manager


class User(AbstractUser):
  username = None
  email = models.EmailField(unique=True)
  bio = models.CharField(max_length=255)
  avatar = models.ImageField(null=True, blank=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = Manager()

  def __str__(self):
    return self.email
