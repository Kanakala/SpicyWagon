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
    
class RestaurantListAPIView(ListAPIView):
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