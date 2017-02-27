from django import forms


from .models import Restaurant, Menu, Dish


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ["Restaurant", "Image", "Address", "Area", "City", "Pin_Code", "Cuisine", "Minimum_Rate", "Time_To_Delivery", "Phone",
            ]
        

class MenuForm(forms.ModelForm):
    #Restaurant = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = Menu
        fields = ["Menu", 
            ]
        
        
        
class DishForm(forms.ModelForm):
    #Restaurant = forms.CharField(widget=forms.HiddenInput)
    #Menu = forms.CharField(widget=forms.HiddenInput)
    class Meta:
        model = Dish
        fields = ["Dish", "Price", "Image",
            ]
        

