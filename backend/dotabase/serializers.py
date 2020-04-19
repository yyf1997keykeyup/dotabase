from rest_framework import serializers
from dotabase.models import *


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


