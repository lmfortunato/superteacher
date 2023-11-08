from django.urls import path
from super_teacher.views import profile, dashboard, create_service, search_service

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('dashboard/', dashboard, name="dashboard"),
    path('create-service/', create_service, name="service"),
    path('search-service/', search_service, name="search_service")
]
