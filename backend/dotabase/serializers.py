from rest_framework import serializers
from dotabase.models import *


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjHero
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authuser
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjHeroLog
        fields = '__all__'

