import django_filters
from dotabase.models import *
from dotabase.serializers import  *

class HeroFilter(django_filters.rest_framework.FilterSet):
    hero_id = django_filters.CharFilter(field_name="hero_id")
    name = django_filters.CharFilter(field_name="name")
    bio = django_filters.CharFilter(field_name="bio")

    class Meta:
        model = ProjHero
        fields = ['name', 'bio',]


class UserFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(field_name="username")
    password = django_filters.CharFilter(field_name="password")

    class Meta:
        model = AuthUser
        fields = ['username', 'password',]

class LogFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.CharFilter(field_name="hero_id")

    class Meta:
        model = ProjHeroLog
        fields = ['hero_id']