from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.contrib.auth.models import User
from django import forms
from .models import CartItem

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'type': 'number', 'value': '1', 'min':'1', 'max': '99',
            'class': 'form-control input-sm',
        })
    )
    update = forms.BooleanField(required=False, initial=False, widget = forms.HiddenInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_id'] = forms.IntegerField(widget=forms.HiddenInput())
        
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 1:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity