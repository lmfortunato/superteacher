from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    subject = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    price = models.IntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.subject}"