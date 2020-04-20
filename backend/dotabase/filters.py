import django_filters
from dotabase.models import *
from dotabase.serializers import  *

class HeroFilter(django_filters.rest_framework.FilterSet):
    heroid = django_filters.CharFilter(field_name="heroid")
    name = django_filters.CharFilter(field_name="name")
    bio = django_filters.CharFilter(field_name="bio")

    class Meta:
        model = ProjHero
        fields = ['name', 'bio',]