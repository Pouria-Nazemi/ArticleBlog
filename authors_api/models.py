from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

class User(AbstractUser):
    email = models.EmailField(null = False, blank = False)
    blog = models.URLField(null = True, blank = True)

    objects = UserManager()
