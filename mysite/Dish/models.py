from django.db import models
from Restaurant.models import Restaurant
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


    
class DishManager(models.Manager):
    def all(self):
        dqs = super(DishManager, self)
        return dqs

    def filter_by_instance(self, menu_instance):
        menu_type = ContentType.objects.get_for_model(menu_instance.__class__)
        obj_did = menu_instance.id
        dqs = super(DishManager, self).filter(menu_type=menu_type, menu_id= obj_did)
        return dqs

    def create_by_model_type(self, model_type, id, Dish, user):
        model_dqs = ContentType.objects.filter(model=model_type)
        if model_dqs.exists():
            SomeModel = model_dqs.second().model_class()
            obj_dqs = SomeModel.objects.filter(id=id)
            if obj_dqs.exists() and obj_dqs.count() == 1:
                menu_instance = self.model()
                menu_instance.Dish = Dish
                menu_instance.Restaurant= obj_dqs.first().Restaurant
                menu_instance.restaurant_id = obj_dqs.first().id
                menu_instance.Restaurant = user
                menu_instance.user = user
                menu_instance.menu_type = model_dqs.second()
                menu_instance.menu = obj_dqs.second().Menu
                menu_instance.menu_id = obj_dqs.second().id
                #if parent_obj:
                  #  instance.parent = parent_obj
                menu_instance.save()
                return menu_instance
        return None

    
class Dish(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="dish_users")
    menu_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="menus")
    menu_id = models.PositiveIntegerField()
    menu_object = GenericForeignKey('menu_type', 'menu_id')
    #parent = models.ForeignKey("Menu", null=True, blank=True)
    Restaurant = models.CharField(max_length=30)
    restaurant_id = models.PositiveIntegerField()
    Menu = models.CharField(max_length=50)
    Dish = models.CharField(max_length=50)
    Price = models.CharField(max_length=4)
    
    def __unicode__(self):
        return self.Dish

    def __str__(self):
        return self.Dish
