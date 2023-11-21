from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from super_teacher.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", dashboard, name="dashboard"),
    path("home/", include("super_teacher.urls")),
    path("accounts/", include("profiles.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)