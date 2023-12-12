from django.db import models

class Customer(models.Model):
    email = models.EmailField(unique=True)

class Hotel(models.Model):
    email = models.EmailField(unique=True)

# Create your models here.
