from rest_framework import serializers
from dotabase.models import *
from django.contrib.auth.models import User


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjHero
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjHeroLog
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, data):
        return data
