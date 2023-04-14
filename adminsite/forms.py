from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import ProductCategory, Product, Profile, Brand

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['category_name', 'description']
        
class EditProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['category_name', 'description']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name', 'description']
        
class EditBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name', 'description']    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category_name', 'brand_name', 'name', 'image', 
                  'color', 'price', 'quantity', 'detail1', 
                  'detail2', 'detail3', 'description']