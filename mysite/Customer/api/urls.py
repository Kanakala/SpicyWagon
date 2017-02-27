from django.conf.urls import url
from django.contrib import admin

from .views import (
    RestaurantCreateAPIView,
    RestaurantListAPIView,
    RestaurantDetailAPIView,
    RestaurantUpdateAPIView,
    RestaurantDeleteAPIView,
    MenuDetailAPIView,
    MenuUpdateAPIView,
    MenuDeleteAPIView,
    DishDetailAPIView,
    DishUpdateAPIView,
    DishDeleteAPIView,
    MenuCreateAPIView,
    DishCreateAPIView,
    
    )

urlpatterns = [
    url(r'^$', RestaurantListAPIView.as_view(), name='list'),
    url(r'^create/$', RestaurantCreateAPIView.as_view(), name='create'),
    url(r'^menu_create/$', MenuCreateAPIView.as_view(), name='menu_create'),
    url(r'^dish_create/$', DishCreateAPIView.as_view(), name='dish_create'),
    url(r'^(?P<slug>[\w-]+)$', RestaurantDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', RestaurantUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', RestaurantDeleteAPIView.as_view(), name='delete'),
    url(r'^menu/(?P<id>[\w-]+)$', MenuDetailAPIView.as_view(), name='menu_detail'),
    url(r'^menu/(?P<id>[\w-]+)/edit/$', MenuUpdateAPIView.as_view(), name='menu_update'),
    url(r'^menu/(?P<id>[\w-]+)/edit/$', MenuDeleteAPIView.as_view(), name='menu_delete'),
    url(r'^dish/(?P<id>[\w-]+)$', DishDetailAPIView.as_view(), name='dish_detail'),
    url(r'^dish/(?P<id>[\w-]+)/edit/$', DishUpdateAPIView.as_view(), name='dish_update'),
    url(r'^dish/(?P<id>[\w-]+)/edit/$', DishDeleteAPIView.as_view(), name='dish_delete'),
    
]