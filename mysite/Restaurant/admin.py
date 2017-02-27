from django.contrib import admin
from django.db import models
from .models import Restaurant, SubMenu, Dish, Menu


class DishInline(admin.TabularInline):
    model = Dish
    raw_id_fields = ("Restaurant",)


class RestaurantModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("Restaurant", "Area", "City",)}
    list_display = ["Restaurant", "City", "City_Code", "Area", "Cuisine", "Minimum_Rate", "Time_To_Delivery", "Phone", ]
    list_display_links = ["Restaurant",]
    list_editable = [ "Cuisine", "City_Code",  "Minimum_Rate", "Time_To_Delivery",]
    list_filter = ["City", "Area", "Minimum_Rate", "Time_To_Delivery",]
    

    search_fields = ["Restaurant",]
    inlines = [
        DishInline,
    ]
    class Meta:
            model = Restaurant

admin.site.register( Restaurant, RestaurantModelAdmin)

class MenuModelAdmin(admin.ModelAdmin):
    
    inlines = [
        DishInline,
    ]
	
    class Meta:
        model = Menu

admin.site.register( Menu, MenuModelAdmin)


class SubMenuModelAdmin(admin.ModelAdmin):
    
    inlines = [
        DishInline,
    ]
	
    class Meta:
        model = SubMenu

admin.site.register( SubMenu, SubMenuModelAdmin)


class DishModelAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Dish

admin.site.register( Dish, DishModelAdmin)



