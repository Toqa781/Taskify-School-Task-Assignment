# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CreateUserForm(UserCreationForm):
    role = forms.ChoiceField(choices=Profile.USER_ROLES, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "role"]
