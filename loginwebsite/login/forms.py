from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):




    class meta:
        model = User
        fields =['username','password1','password2','email']


class EditProfile(UserChangeForm):
    class Meta:
        model=User
        fields=[

            'email',
            'first_name',
            'last_name',
        ]