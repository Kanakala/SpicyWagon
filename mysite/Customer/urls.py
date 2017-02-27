from django.conf.urls import url
from django.contrib import admin

from Restaurant.views import (
	
	restaurant_detail,
)

from Customer.views import(
	restaurant_list,
	pnr_restaurants,
	train_restaurants,
	pnr_restaurant_json,
	train_restaurant_json,
	index,
	restaurant_json,
	dish_json)

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^restaurant_list/$', restaurant_list, name='restaurant_list'),
	url(r'^restaurant_json/$', restaurant_json, name='restaurant_json'),
	url(r'^pnr_restaurant_json/(?P<id>\d+)/$', pnr_restaurant_json, name='pnr_rest_json'),
	url(r'^train_restaurant_json/(?P<id>\d+)/$', train_restaurant_json, name='train_rest_json'),
	url(r'^dish_json/(?P<slug>[\w-]+)/$', dish_json, name='dish_json'),
	url(r'^restaurants/pnr/(?P<id>\d+)/$', pnr_restaurants, name='pnr_rest_list'),
	url(r'^restaurants/train/(?P<id>\d+)/$', train_restaurants, name='train_rest_list'),
]
    #url(r'^(?P<slug>[\w-]+)/$', OrderCreateView.as_View(), name='detail'),
    
