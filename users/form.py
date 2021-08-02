from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # change this, if you are using a custom model

class RegisterUserForm(UserCreationForm):
    """subclassing from the UserCreationForm"""
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        # other django default params you can add are: first_name, last_name to the fields.
