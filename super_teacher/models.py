from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)

class Professor(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone_number = models.IntegerField()
    photo = models.CharField(blank=True, max_length=256)

class Service(models.Model):
    subject = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    price = models.IntegerField()