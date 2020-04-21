from django.shortcuts import render, redirect

# Create your views here.
from register.models import *
from register.serializers import *
from register.filters import *
from rest_framework import generics
from rest_framework import filters
import django_filters


class UserRegister(generics.ListCreateAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filter_class = UserFilter
    search_fields = ('name', 'password',)