from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'role', 'phone_number',
            'gender', 'profile_picture',
            'password1', 'password2',
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'role', 'phone_number',
            'gender', 'profile_picture',
        )

