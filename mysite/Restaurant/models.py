from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class RestaurantManager(models.Manager):
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return super(RestaurantManager, self)

def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    RestaurantModel = instance.__class__
    new_id = RestaurantModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)

class Restaurant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    Restaurant = models.CharField(max_length=40)
    slug = models.SlugField(unique=True)
    Image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True )
    image_path = models.CharField(max_length=200, null=True, blank=True)
    Address = models.TextField(max_length=200)
    Area = models.CharField(max_length=40)
    City = models.CharField(max_length=40)
    City_Code = models.CharField(max_length=6)
    Pin_Code = models.CharField(max_length=10)
    Cuisine = models.CharField(max_length=500)
    Minimum_Rate = models.CharField(max_length=4)
    Time_To_Delivery = models.CharField(max_length=3)
    Phone = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.Restaurant

    def __str__(self):
        return self.Restaurant
    
    def get_absolute_url(self):
        return reverse("restaurants:detail", kwargs={"slug": self.slug})
    
    def get_api_url(self):
        return reverse("restaurants-api:detail", kwargs={"slug": self.slug})
		
    def get_dish_json(self):
        return reverse("customers:dish_json", kwargs={"slug": self.slug})
    
    
    
    
def create_slug(instance, new_slug=None):
    slug = slugify(instance.Restaurant + "-" +instance.Area + "-" +instance.City)
    if new_slug is not None:
        slug = new_slug
    qs = Restaurant.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

    


pre_save.connect(pre_save_post_receiver, sender=Restaurant)

def create_image_path(instance, new_image_path=None):
    image_path = "127.0.0.1:8000" + "/" + "media" + "/" + str(instance.id) + "/" + str(instance.Image)
    if new_image_path is not None:
        image_path = image_path
    qs = Restaurant.objects.filter(image_path=image_path).order_by("-id")
    exists = qs.exists()
    if exists:
        new_image_path = "%s-%s" %(image_path, qs.first().id)
        return create_image_path(instance, new_image_path=new_image_path)
    return image_path

def pre_save_image_receiver(sender, instance, *args, **kwargs):
    if not instance.image_path:
        instance.image_path = create_image_path(instance)

    


pre_save.connect(pre_save_image_receiver, sender=Restaurant)


class Menu(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    Restaurant = models.ForeignKey(Restaurant, default=1, related_name="menu_restaurant")
    Menu = models.CharField(max_length=30)
    no = models.IntegerField()
    
    
    def __unicode__(self):
        return self.Menu

    def __str__(self):
        return self.Menu
    
    def get_absolute_url(self):
        return reverse("restaurants:thread", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("restaurants:delete", kwargs={"id": self.id})
		

class SubMenu(models.Model):

	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
	Restaurant = models.ForeignKey(Restaurant, related_name="submenu_restaurant")
	Menu = models.ForeignKey(Menu, related_name="submenu_menu")
	Sub_Menu = models.CharField(max_length=30)
	no = models.IntegerField()
	
	def __unicode__(self):
		return self.Sub_Menu

	def __str__(self):
		return self.Sub_Menu
    

    
class Dish(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
	Restaurant = models.ForeignKey(Restaurant, related_name="dish_restaurant")
	Menu = models.ForeignKey(Menu, related_name="dish_menu")
	Sub_Menu = models.ForeignKey(SubMenu, null=True, blank=True, related_name="dish_submenu")
	Dish = models.CharField(max_length=50)
	Image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True )
	image_path = models.CharField(max_length=200, null=True, blank=True)
	Price = models.CharField(max_length=4)
    
	def __unicode__(self):
		return self.Dish

	def __str__(self):
		return self.Dish
		
		
def pre_save_image_receiver(sender, instance, *args, **kwargs):
    if not instance.image_path:
        instance.image_path = create_image_path(instance)

    


pre_save.connect(pre_save_image_receiver, sender=Dish)
    
    

    

    

