from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(required=True, max_length=64)
    password = forms.CharField(required=True, max_length=10)

class ProfileForm(forms.Form):
    name = forms.CharField(required=True, max_length=64)
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)
    # photo = forms.CharField(required=False, max_length=256)

class CreateServiceForm(forms.Form):
    subject = forms.CharField(required = True, max_length=64)
    description = forms.CharField(required = True, max_length=256, widget=forms.Textarea)
    price = forms.IntegerField(required = True, max_value=300)