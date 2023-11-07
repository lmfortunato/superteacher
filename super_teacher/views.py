from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from super_teacher.models import User, Professor, Service
from super_teacher.forms import SignUpForm, ProfileForm, CreateServiceForm

def dashboard(request):
    context = {
        'services' : Service.objects.all()
    }
    http_response = render(
        request = request, 
        template_name = "super_teacher/dashboard.html",
        context = context
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

            successful_url = reverse('login')
            return redirect(successful_url)

    else:
        form = SignUpForm()
    http_response = render(
        request = request,
        template_name = 'super_teacher/sign-up.html',
        context = {'form' : form}
    )
    return http_response

def login(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            username = data["username"]
            password = data["password"]

            users = User.objects.all()
            for user in users:
                if user.username == username and user.password == password:
                    user_found = user
                    successful_url = reverse('dashboard')
                    return redirect(successful_url)
            failed_login = render(
                request = request,
                template_name = 'super_teacher/login.html',
                context = {'error': "Authentication failed, try again", 'form' : form}
            )
            return failed_login
    else:
        form = SignUpForm()
    http_response = render(
        request = request,
        template_name = 'super_teacher/login.html',
        context = {'form' : form}
    )
    return http_response

def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            name = data["name"]
            email = data["email"]
            phone_number = data["phone_number"]
            # photo = data["photo"]

            new_professor = Professor(name = name, email = email, phone_number = phone_number)
            new_professor.save()

            successful_url = render(
                request = request,
                template_name = 'super_teacher/profile.html',
                context = {'professor' : new_professor}
            )
            return successful_url

    else:
        form = ProfileForm()
    http_response = render(
        request = request,
        template_name = 'super_teacher/profile.html',
        context = {'form' : form, 'image': 'assets/avatar.png'}
    )
    return http_response

def create_service(request):
    if request.method == "POST":
        form = CreateServiceForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            subject = data["subject"]
            description = data["description"]
            price = data["price"]

            new_service = Service(subject = subject, description = description, price = price)
            new_service.save()

            successful_url = reverse('dashboard')
            return redirect(successful_url)

    else:
        form = CreateServiceForm()
    http_response = render(
        request = request,
        template_name = 'super_teacher/create-service.html',
        context = {'form' : form}
    )
    return http_response

# def list_services(request):
#     context = {
#         'services' : Service.objects.all()
#     }
#     http_response = render(
#         request = request, 
#         template_name = 'super_teacher/dashboard.html',
#         context = context
#     )
#     return http_response