from django.db import models
from django.conf import settings
from Restaurant.models import Restaurant, Menu, Dish
from django.core.urlresolvers import reverse

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    #Restaurant = models.ForeignKey(Restaurant)
    #Menu = models.ForeignKey(Menu)
    Dish = models.ForeignKey(Dish)
    Count = models.IntegerField()
    Dish_Price = models.CharField(max_length=4)
    Total_Amount = models.CharField(max_length=5)
    Confirmed = models.BooleanField(default = False)
    
class Total_Orders(models.Model):
    Order = models.ForeignKey(Order)
    Dish = models.CharField(max_length=30)
    Dish_Price = models.CharField(max_length=4)
    Total_Amount = models.CharField(max_length=5)
	
class Search(models.Model):
	Pnr = models.CharField(max_length=10, null=True, blank=True)
	TrainDetails = models.CharField(max_length=30, null=True, blank=True)
	Date = models.CharField(max_length=20, null=True, blank=True)
	Boarding = models.CharField(max_length=20, null=True, blank=True)
	TimeStamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
class PnrSearch(models.Model):
	Pnr = models.CharField(max_length=10)
	TimeStamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	def __unicode__(self):
		return self.Pnr

	def __str__(self):
		return self.Pnr
	
	def get_absolute_url(self):
		return reverse("customers:pnr_rest_list", kwargs={"id": self.id})
	
class TrainSearch(models.Model):
	TrainDetails = models.CharField(max_length=30)
	Date = models.CharField(max_length=30)
	Boarding = models.CharField(max_length=30, null=True, blank=True)
	TimeStamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	def __unicode__(self):
		return self.TrainDetails

	def __str__(self):
		return self.TrainDetails
	
	def get_absolute_url(self):
		return reverse("customers:train_rest_list", kwargs={"id": self.id})
	
	
	
    
