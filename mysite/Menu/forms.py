from django import forms


from .models import Menu

class MenuForm(forms.ModelForm):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = Menu
        fields = ["Menu",
            ]
        
