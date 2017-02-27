from django import forms
from django.forms.formsets import BaseFormSet
from .models import PnrSearch, TrainSearch


# class BaseOrderFormSet(BaseFormSet):
    
    # Counts = []
    # Dish_Prices = []
    # Total_Amounts = []
    # duplicates = True
    
    # for form in self.forms:
        # if form.cleaned_data:
            #Dish = form.cleaned_data['Dish']
            # Count = form.cleaned_data['Count']
            # Dish_Price = form.cleaned_data['Dish_Price']
            # Total_Amount = form.cleaned_data['Total_Amount']
            
            # if Count, Dish_Price and Total_Amount:
                    # if Count in Counts:
                        # duplicates = True
                    # Counts.append(Count)

                    # if Dish_Price in Dish_Prices:
                        # duplicates = True
                    # Dish_Prices.append(Dish_Price)
                    
                    # if Total_Amount in Total_Amounts:
                        # duplicates = True
                    # Total_Amounts.append(Total_Amounts)
					
# class SearchForm(forms.ModelForm):

	# Pnr = forms.CharField(required=False)
	# TrainDetails = forms.CharField(required=False, label='Train Details')
	# Date = forms.CharField(required=False)
	# Boarding = forms.CharField(required=False)
	# class Meta:
		# model = Search
		# fields = ['Pnr', 'TrainDetails', 'Date', 'Boarding',]
		
	# def clean(self):
		# cleaned_data = super(SearchForm, self).clean()
		# TrainDetails = cleaned_data.get("TrainDetails")
		# Date = cleaned_data.get("Date")
		# if TrainDetails and not Date:
			# raise forms.ValidationError("Date is a required field.")
		# if Date and not TrainDetails:
			# raise forms.ValidationError("Train Details is a required field.")
		# return cleaned_data
		
class PnrSearchForm(forms.ModelForm):
	Pnr = forms.CharField(max_length=10, label = 'PNR Number')
	class Meta:
		model = PnrSearch
		fields = ['Pnr',]
		
class TrainSearchForm(forms.ModelForm):
	TrainDetails = forms.CharField(max_length=30, label = 'Train No/Name')
	Boarding = forms.CharField(max_length=30, label = 'Boarding Station')
	Date = forms.CharField(max_length=30, label = 'Date')
	class Meta:
		model = TrainSearch
		fields = ['TrainDetails', 'Date', 'Boarding',]

