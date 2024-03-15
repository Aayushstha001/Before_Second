from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ['address', 'phone_no']