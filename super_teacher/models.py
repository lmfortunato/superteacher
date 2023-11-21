from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=8)

#     def __str__(self):
#         return f"{self.username}"

# class Professor(models.Model):
#     name = models.CharField(max_length=64)
#     email = models.EmailField()
#     phone_number = models.IntegerField()
#     # photo = models.CharField(blank=True, max_length=256)

#     def __str__(self):
#         return f"Professor: {self.name}"

class Service(models.Model):
    subject = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    price = models.IntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.subject}"