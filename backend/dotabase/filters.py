import django_filters
from dotabase.models import *
from dotabase.serializers import  *

class HeroFilter(django_filters.rest_framework.FilterSet):
    hero_id = django_filters.CharFilter(field_name="hero_id")
    name = django_filters.CharFilter(field_name="name")
    bio = django_filters.CharFilter(field_name="bio")

    class Meta:
        model = Hero
        fields = ['name', 'bio',]