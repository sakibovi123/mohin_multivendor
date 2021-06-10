from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from store.models import *


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']