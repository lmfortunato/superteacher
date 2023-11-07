from django.urls import path
from super_teacher.views import profile, dashboard

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('dashboard/', dashboard, name="dashboard")
]
