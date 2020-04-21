from django.shortcuts import render
from rest_framework import *
from rest_framework import generics
from rest_framework import filters
import django_filters
from dotabase.models import *
from dotabase.serializers import *
from dotabase.filters import *


# Create your views here.
class HeroList(generics.ListCreateAPIView):
    queryset = ProjHero.objects.all()
    serializer_class = HeroSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filter_class = HeroFilter
    search_fields = ('name', 'bio',)


class HeroUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjHero.objects.all()
    serializer_class = HeroSerializer



class UserRegister(generics.ListCreateAPIView):
    queryset = Authuser.objects.all()
    serializer_class = UserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filter_class = UserFilter
    search_fields = ('name', 'password',)

class LogRegister(generics.ListCreateAPIView):
    queryset = ProjHeroLog.objects.all()
    serializer_class = LogSerializer

