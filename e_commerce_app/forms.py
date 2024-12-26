from django import forms
from .models import User
import re

class SignupForm(forms.Form):
    firstname = forms.CharField(max_length=100, required=True)
    lastname = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField( widget=forms.EmailInput)
    password = forms.CharField(required=True)

    def clean_username(self):
        name = self.cleaned_data.get('username')
        if len(name) < 5:
            raise forms.ValidationError('Username must be more than 5 characters long')
        return name
    
    def clean_username(self):
        username = self.cleaned_data('username')
        if User.objects.exists(username=username):
            raise forms.ValidationError('username already exists, try again')
        return username
    
    def clean_email(self):
        email = self.cleaned_data('email')
        if User.objects.exists(email=email):
            raise forms.ValidationError('username already exists, try again')
        return email
    
    def clean_password(self):
        password = self.cleaned_data('password')
        if len(password) < 8:
            raise forms.ValidationError('password must be more than 8 characters')
        return 
    
class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)
    quantity = forms.IntegerField(required=True)
    image = forms.ImageField(required=True)
    description = forms.Textarea()
    discount = forms.FloatField(required=False)


class ReviewForm(forms.Form):
    rating = forms.IntegerField()
    comment = forms.Textarea()