from django.shortcuts import render

# Create your views here.
from .models import Contact
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ContactSerializer


class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]