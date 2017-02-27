from django.db import models
from Restaurant.models import Restaurant
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class MenuManager(models.Manager):
    
   
    
    def all(self):
        mqs = super(MenuManager, self)
        return mqs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_mid = instance.id
        mqs = super(MenuManager, self).filter(content_type=content_type, restaurant_id= obj_mid)
        return mqs

    def create_by_model_type(self, model_type, slug, Menu, user):
        model_mqs = ContentType.objects.filter(model=model_type)
        if model_mqs.exists():
            SomeModel = model_mqs.first().model_class()
            obj_mqs = SomeModel.objects.filter(slug=slug)
            if obj_mqs.exists() and obj_mqs.count() == 1:
                instance = self.model()
                instance.Menu = Menu
                instance.Restaurant = obj_mqs.first().Restaurant
                instance.user = user
                instance.content_type = model_mqs.first()
                instance.restaurant_id = obj_mqs.first().id
                
                #if parent_obj:
                   # instance.parent = parent_obj
                instance.save()
                return instance
        return None

class Menu(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="menu_users")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="restaurants")
    Restaurant = models.CharField(max_length=30)
    restaurant_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'restaurant_id')
    #parent = models.ForeignKey("self", null=True, blank=True)
    #Restaurant = models.ForeignKey("Restaurant", null=True, blank=True)
    Menu = models.CharField(max_length=30)
    
    objects = MenuManager()
    
    def __unicode__(self):
        return self.Menu

    def __str__(self):
        return self.Menu
    
    def get_absolute_url(self):
        return reverse("menus:thread", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("menus:delete", kwargs={"id": self.id})
    
    @property
    def dishes(self):
        menu_instance = self
        dqs = Menu.objects.filter_by_instance(menu_instance)
        return dqs

    @property
    def get_menu_type(self):
        menu_instance = self
        mmenu_type = ContentType.objects.get_for_model(menu_instance.__class__)
        return menu_type
        
    #def children(self): #dishes
        #return Menu.objects.filter(parent=self)

   # @property
   # def is_parent(self):
      #  if self.parent is not None:
       #     return False
      #  return True
    
