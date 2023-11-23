from django.urls import path
from super_teacher.views import (
    profile, dashboard, create_service, search_service, delete_service, edit_service, ServiceDetailView, about_me
    )

urlpatterns = [
    path('profile/', profile, name="profile"),
    # path('dashboard/', dashboard, name="dashboard"),
    path('create-service/', create_service, name="service"),
    path('search-service/', search_service, name="search_service"),
    path('delete-service/<int:id>', delete_service, name="delete_service"),
    path('edit-service/<int:id>', edit_service, name="edit_service"),
    path('about-me', about_me, name="about_me"),
    path("service/<int:pk>", ServiceDetailView.as_view(), name="service_detail")
]
