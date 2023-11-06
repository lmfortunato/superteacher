from django.contrib import admin
from django.urls import path

from django_project.views import index
from super_teacher.views import sign_up, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("sign-up/", sign_up, name="sign_up"),
    path("home/", home, name="home")
]
