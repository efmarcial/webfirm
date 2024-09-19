from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create a ModelForm
class QuoteForm(forms.ModelForm):
    # specify the name of model to user
    class Meta:
        model = QuoteRequest
        fields = "__all__"
        
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'email', 'password1', 'password2')