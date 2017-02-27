from rest_framework.generics import (ListAPIView, 
                                     RetrieveAPIView, 
                                     UpdateAPIView, 
                                     DestroyAPIView, 
                                     CreateAPIView)
from Restaurant.models import Restaurant, Menu, Dish
from .serializers import (RestaurantListSerializer, 
                          RestaurantDetailSerializer, 
                          RestaurantCreateSerializer,
                          RestaurantUpdateSerializer,
                          MenuCreateSerializer,
                          MenuDetailSerializer,
                          MenuUpdateSerializer,
                          DishDetailSerializer,
                          DishUpdateSerializer,
                          DishCreateSerializer)
from custom_user.models import EmailUser
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_jsonp.renderers import JSONPRenderer, JSONRenderer
from django.http import HttpResponse


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data, renderer_context={'indent':4})
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class CustomListModelMixin(ListModelMixin):
	
	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		
		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(queryset, many=True)
		return Response({'results': serializer.data})

class RestaurantCreateAPIView(CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer
    
    
    #def perform_create(self, serializer):
        #serializer.save(user=self.request.user)

class RestaurantDeleteAPIView(DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    lookup_field = 'slug'

class RestaurantDetailAPIView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    lookup_field = 'slug'
    
class RestaurantListAPIView(CustomListModelMixin, ListAPIView):
    
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
	
		
    
class RestaurantUpdateAPIView(UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantUpdateSerializer
    lookup_field = 'slug'
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
class MenuCreateAPIView(CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuCreateSerializer
    
class MenuDetailAPIView(RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuDetailSerializer
    lookup_field = 'id'

class MenuUpdateAPIView(UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuUpdateSerializer
    lookup_field = 'id'
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
class MenuDeleteAPIView(DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = MenuDetailSerializer
    lookup_field = 'id'
    
class DishCreateAPIView(CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishCreateSerializer

class DishDetailAPIView(RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishDetailSerializer
    lookup_field = 'id'

class DishUpdateAPIView(UpdateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishUpdateSerializer
    lookup_field = 'id'
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
class DishDeleteAPIView(DestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishDetailSerializer
    lookup_field = 'id'