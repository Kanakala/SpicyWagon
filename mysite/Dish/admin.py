from django.contrib import admin
from django.db import models
from .models import  Dish



class DishModelAdmin(admin.ModelAdmin):
    
    class Meta:
            model = Dish

admin.site.register( Dish, DishModelAdmin)
