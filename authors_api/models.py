from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

class User(AbstractUser):
    email = models.EmailField(null = False, blank = False)
    blog = models.URLField(null = True, blank = True)

    objects = UserManager()

class Article(models.Model):
    title = models.CharField(max_length = 300,blank = False, null = False)
    description = models.TextField(blank = False, null = False)
    link = models.URLField(blank = False, null = False)
    date_modified = models.DateField(auto_now = True)
    subject = models.CharField(max_length = 50, blank = False, null = False)
    author_id = models.ForeignKey(User, on_delete = models.CASCADE)



    
