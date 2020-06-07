from django.contrib import admin
from django.contrib.admin import register
from . import models
# Register your models here.

admin.site.register(models.Todo)
admin.site.register(models.Types)