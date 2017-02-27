from django.conf.urls import url
from django.contrib import admin

from .views import (
	
	restaurant_create,
	restaurant_detail,
	restaurant_list,
	restaurant_delete,
    menu_thread,
    menu_delete

	)

urlpatterns = [
	#url(r'^$', restaurant_list, name='list'),
    url(r'^create/$', restaurant_create),
    url(r'^detail/(?P<slug>[\w-]+)/$', restaurant_detail, name='detail'),
    #url(r'^(?P<slug>[\w-]+)/editc/$', restaurant_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', restaurant_delete),
    url(r'^(?P<id>\d+)/$', menu_thread, name='thread'),
    url(r'^(?P<id>\d+)/delete/$', menu_delete, name='menu_delete'),
    #url(r'^restaurants/$', "<appname>.views.<function_name>"),
]