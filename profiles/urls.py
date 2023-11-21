from django.urls import path
from profiles.views import sign_up, login_view, CustomLogoutView, ProfileUpdateView, add_avatar, update_avatar

urlpatterns = [
    path('sign-up/', sign_up, name="sign_up"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('profile-update/', ProfileUpdateView.as_view(), name="profile_update"),
    path('add-avatar/', add_avatar, name="add_avatar"),
    path('update-avatar/<int:id>', update_avatar, name="update_avatar"),
]