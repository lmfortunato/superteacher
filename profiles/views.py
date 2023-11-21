from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from profiles.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from profiles.forms import UserRegisterForm, UserUpdateForm, AvatarForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from profiles.models import Avatar
from super_teacher.models import Service
from django.contrib.auth.decorators import login_required

def sign_up(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            successful_url = reverse('dashboard')
            return redirect(successful_url)
    else:
        form = UserRegisterForm()
    return render(
        request=request,
        template_name='profiles/sign-up.html',
        context={'form' : form}
    )

def login_view(request):
    next_url = request.GET.get('next') 
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username = username, password = password)

            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                successful_url = reverse('dashboard')
                return redirect(successful_url)
    else:
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='profiles/login.html',
        context={'form' : form}
    )

class CustomLogoutView(LogoutView):
    template_name = 'profiles/logout.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    success_url = reverse_lazy('profile')
    template_name = 'super_teacher/profile.html'

    def get_object(self, queryset=None):
        return self.request.user

@login_required
def add_avatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            # Creo avatar en la base de datos
            avatar = form.save()
            # Vinculo al avatar con su usuario y guardo
            avatar.user = request.user
            avatar.save()
            successful_url = reverse('profile')
            return redirect(successful_url)
    else:
        form = AvatarForm()
    return render(
        request=request,
        template_name='super_teacher/profile.html',
        context={'formAvatar' : form}
    )

def update_avatar(request, id):
    user = request.user
    avatar = Avatar.objects.get(id=id)

    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES, instance=avatar)

        if form.is_valid():
            # Save the form, which updates the existing avatar
            form.save()
            successful_url = reverse('profile')
            return redirect(successful_url)
    else:
        form = AvatarForm(instance=avatar)

    return render(
        request=request,
        template_name='super_teacher/profile.html',
        context={'formAvatar': form, 'services' : Service.objects.filter(creator = user)}
    )