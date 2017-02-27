from django.contrib import admin
from django.db import models
from .models import TrainSearch, PnrSearch
# Register your models here.


class TrainSearchModelAdmin(admin.ModelAdmin):

    class Meta:
        model = TrainSearch

admin.site.register( TrainSearch, TrainSearchModelAdmin)

class PnrSearchModelAdmin(admin.ModelAdmin):
    
	class Meta:
		model = PnrSearch

admin.site.register( PnrSearch, PnrSearchModelAdmin)