from rest_framework import serializers
from dotabase.models import *
from django.contrib.auth.models import User


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjHero
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    hero_name = serializers.CharField(source='hero.name')
    class Meta:
        model = ProjHeroLog
        fields = ('hero', 'hero_name', 'attr_health', 'attr_maga', 'attr_damage', 'create_time')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, data):
        return data
