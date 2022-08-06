from django import forms

from .models import Customer, Rider

class RiderForm(forms.ModelForm):
    class Meta:
        model = Rider
        exclude = ["user"]
        
        
class CustomerrForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ["user"]