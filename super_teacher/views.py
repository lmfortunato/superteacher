from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from super_teacher.models import User
from super_teacher.forms import SignUpForm

def home(request):
    http_response = render(
        request = request, 
        template_name = "super_teacher/home.html"
    )
    return http_response

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            username = data["username"]
            password = data["password"]

            new_user = User(username = username, password = password)
            new_user.save()

            successful_url = reverse('home')
            return redirect(successful_url)

    else:
        form = SignUpForm()
    http_response = render(
        request = request,
        template_name = 'super_teacher/sign-up.html',
        context = {'form' : form}
    )
    return http_response

