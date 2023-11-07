from django.contrib import admin
from django.urls import path, include

from django_project.views import index
from super_teacher.views import sign_up, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("sign-up/", sign_up, name="sign_up"),
    path("login/", login, name="login"),
    path("home/", include("super_teacher.urls"))
    # path("", .as_view(), name="")
]
