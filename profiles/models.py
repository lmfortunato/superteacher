from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

class Avatar(models.Model):
    # Avatar es una tabla relacionada con User
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # upload_to es la subcarpeta dentro de la carpeta media
    image =  models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return f"Avatar from: {self.user}"