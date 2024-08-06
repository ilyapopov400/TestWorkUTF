from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.FoodCategory)

admin.site.register(models.Food)
