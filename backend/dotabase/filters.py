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


# class UserFilter(django_filters.rest_framework.FilterSet):
#     name = django_filters.CharFilter(field_name="username")
#     password = django_filters.CharFilter(field_name="password")
#
#     class Meta:
#         model = Authuser
#         fields = ['username', 'password',]

class LogFilter(django_filters.rest_framework.FilterSet):
    #id = django_filters.CharFilter(field_name="logid")
    hero = django_filters.NumberFilter(field_name="hero")
    health = django_filters.CharFilter(field_name="attr_health")
    damage = django_filters.CharFilter(field_name="attr_damage")
    mana = django_filters.CharFilter(field_name="attr_maga")

    class Meta:
        model = ProjHeroLog
        fields = ['hero', 'attr_health', 'attr_damage', 'attr_maga']