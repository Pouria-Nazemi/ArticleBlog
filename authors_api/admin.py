from django.contrib import admin
from authors_api import models

admin.site.register(models.User)
admin.site.register(models.Article)