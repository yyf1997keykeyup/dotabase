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

class ItemFilter(django_filters.rest_framework.FilterSet):
    item_id = django_filters.CharFilter(field_name="itemid")
    item_name = django_filters.CharFilter(field_name="itemname")

    class Meta:
        model = ProjItem
        fields = ['item_name']
    
class HeroGoodAgainstFilter(django_filters.rest_framework.FilterSet):
    heroid_1 = django_filters.CharFilter(field_name="heroid_1")
    heroid_2 = django_filters.CharFilter(field_name="heroid_2")
    hgaid = django_filters.CharFilter(field_name="hgaid")
    
    class Meta:
        model = ProjHerogoodagainst
        fields = ["heroid_1","heroid_2"]

class HeroBadAgainstFilter(django_filters.rest_framework.FilterSet):
    heroid_1 = django_filters.CharFilter(field_name="heroid_1")
    heroid_2 = django_filters.CharFilter(field_name="heroid_2")
    hgaid = django_filters.CharFilter(field_name="hgaid")
    
    class Meta:
        model = ProjHerobadagainst
        fields = ["heroid_1","heroid_2"]

class HeroBestCombosFilter(django_filters.rest_framework.FilterSet):
    heroid_1 = django_filters.CharFilter(field_name="heroid_1")
    heroid_2 = django_filters.CharFilter(field_name="heroid_2")
    hgaid = django_filters.CharFilter(field_name="hgaid")
    
    class Meta:
        model = ProjHerobestcombos
        fields = ["heroid_1","heroid_2"]

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

    