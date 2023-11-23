from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from super_teacher.models import Service
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

@login_required
def profile(request):
    user = request.user
    context = {
        'services' : Service.objects.filter(creator = user)
    }
    http_response = render(
        request = request,
        template_name = 'profiles/profile.html',
        context = context
    )
    return http_response

@login_required
def create_service(request):
    if request.method == "POST":
        form = CreateServiceForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            subject = data["subject"]
            description = data["description"]
            price = data["price"]

            new_service = Service(subject = subject, description = description, price = price, creator = request.user)
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

def search_service(request):
    if request.method == 'POST':
        data = request.POST
        search = data['search']
        # Filter
        services = Service.objects.filter(subject__contains = search)

        context = {
            "services" : services
        }
        http_response = render(
            request=request,
            template_name='super_teacher/dashboard.html',
            context=context
        )
        return http_response
    
def delete_service(request, id):
    service = Service.objects.get(id=id)
    if (request.method == "POST"):
        service.delete()
        successful_url = reverse('dashboard')
        return redirect(successful_url)
    
def edit_service(request, id):
    service = Service.objects.get(id=id)
    if request.method == "POST":
        form = CreateServiceForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            service.subject = data["subject"]
            service.description = data["description"]
            service.price = data["price"]

            service.save()

            successful_url = reverse('dashboard')
            return redirect(successful_url)

    else:
        initial = {
            'subject' : service.subject,
            'description' : service.description,
            'price' : service.price
        }

        form = CreateServiceForm(initial=initial)
    http_response = render(
        request = request,
        template_name = 'super_teacher/create-service.html',
        context = {'form' : form}
    )
    return http_response

def about_me(request):
    http_response = render(
        request =  request,
        template_name = 'super_teacher/about.html'
    )
    return http_response

class ServiceDetailView(DetailView):
    model = Service
    success_url = reverse_lazy('dashboard')