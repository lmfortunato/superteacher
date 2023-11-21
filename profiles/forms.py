from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from profiles.models import Avatar

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']