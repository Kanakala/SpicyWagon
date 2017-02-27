from django import forms


from .models import Dish

        
class DishForm(forms.ModelForm):
    menu_type = forms.CharField(widget=forms.HiddenInput)
    menu_id = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = Dish
        fields = ["Dish", "Price",
            ]