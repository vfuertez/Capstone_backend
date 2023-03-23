from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True, unique=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    