from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(required=True, max_length=64)
    password = forms.CharField(required=True, max_length=10)