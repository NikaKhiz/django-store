from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta():
        model=CustomUser
        fields=['email', 'username', 'password1', 'password2']

    email=forms.EmailField(required=True)    

