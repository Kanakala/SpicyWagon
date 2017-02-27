from django.contrib import admin
from django.db import models
from .models import Menu

class MenuModelAdmin(admin.ModelAdmin):
    
    class Meta:
            model = Menu

admin.site.register( Menu, MenuModelAdmin)

