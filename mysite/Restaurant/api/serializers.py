import json
from django.core import serializers
from rest_framework import serializers
from Restaurant.models import Restaurant, Menu, Dish
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    URLField,
    )



class RestaurantCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Restaurant
        fields = ["Restaurant", "Area", "City", "Address", "Pin_Code", "Cuisine", "Minimum_Rate", "Time_To_Delivery", "Phone", ]

class RestaurantDetailSerializer(serializers.ModelSerializer):
    #url = restaurant_detail_url
    #media_url = HyperlinkedIdentityField(
        #view_name='restaurants-api:detail',
        #lookup_field='slug'
        #)
    Menus = SerializerMethodField()
    Image = SerializerMethodField()
    class Meta:
        model = Restaurant
        fields = ['id', 'Restaurant', 'Image', 'Menus',]
    def get_Menus(self, obj):
        m_qs = Menu.objects.filter(Restaurant=obj)
        Menus = MenuSerializer(m_qs, many=True).data
        return Menus
    def get_Image(self, obj):
        try:
            Image = '127.0.0.1:8000' + obj.Image.url
        except:
            Image = None
        return Image
    

class RestaurantUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Restaurant
        fields =  ["Restaurant", "Address", "Area", "City", "Pin_Code", "Cuisine", "Minimum_Rate", "Time_To_Delivery", "Phone",]
        
class RestaurantListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='restaurants-api:detail',
        lookup_field='slug'
        )
		

    class Meta:
        model = Restaurant
        fields = ["url", "Restaurant", "City",]
		
    def get_queryset(self):
        queryset = Restaurant.objects.all()
        return queryset

    def get_serializer(self):
        serializer = RestaurantListSerializer()
        return serializer
		
    def list(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'results': serializer.data})
        
class DishListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dish
        fields = ['Restaurant', 'Menu', 'Dish', 'Price',]
        

class MenuSerializer(serializers.ModelSerializer):
    Dishes = SerializerMethodField()
    class Meta:
        model = Menu
        fields = ['id', 'Menu', 'Dishes' ]
    def get_Dishes(self, obj):
        d_qs = Dish.objects.filter(Menu=obj)
        Dishes = DishSerializer(d_qs, many=True).data
        return Dishes
    
class MenuDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields =  ["Restaurant", "Menu",]
    
class MenuUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Menu
        fields =  ["Restaurant", "Menu",]
        
class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'Dish', 'Price' ]
        

        
class MenuListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='restaurants-api:menu_list',
        lookup_field='Restaurant'
        )
    class Meta:
        model = Menu
        fields = ['Restaurant', 'Menu',  ]
        
class DishDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields =  ["Restaurant", "Menu", 'Dish', 'Price',]
    
class DishUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dish
        fields =  ["Restaurant", "Menu", 'Dish', 'Price',]
        
class MenuCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Menu
        fields = ['Restaurant', 'Menu',  ]
        
class DishCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dish
        fields = ['Restaurant', 'Menu', 'Dish', 'Price',]

        