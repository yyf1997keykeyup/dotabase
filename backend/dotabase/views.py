from django.shortcuts import render
from rest_framework import *
from rest_framework import generics
from rest_framework import filters
import django_filters
from dotabase.models import *
from dotabase.serializers import *
from dotabase.filters import *
from django.contrib import auth
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
import logging
from dotabase.permission import AdminCheck

logger = logging.getLogger('django')


# Create your views here.
class HeroList(generics.ListCreateAPIView):
    queryset = ProjHero.objects.all()
    serializer_class = HeroSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filter_class = HeroFilter
    search_fields = ('name', 'bio',)


class HeroUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AdminCheck, )
    queryset = ProjHero.objects.all()
    serializer_class = HeroSerializer

    # def put(self, request, pk):
    #     hero = ProjHero.objects.get(pk=pk)
    #     serializer = HeroSerializer(hero, request.data)
    #     if serializer.is_valid():
    #         logger.info("valid hero update")
    #         hero_log = ProjHeroLog(hero=hero, attr_damage=hero.attr_damage, attr_health=hero.attr_health, attr_maga=hero.attr_mana)
    #         hero_log.save()
    #         serializer.save()
    #         return Response({'msg': 'update successful', 'state': True}, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response({'msg': 'add failed'}, status=status.HTTP_400_BAD_REQUEST)


# class UserRegister(generics.ListCreateAPIView):
#     queryset = Authuser.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter)
#     filter_class = UserFilter
#     search_fields = ('name', 'password',)

class LogList(generics.ListAPIView):
    queryset = ProjHeroLog.objects.all()
    serializer_class = LogSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filter_class = LogFilter
    search_fields = ('attr_damage', 'attr_maga', 'attr_health', )

class LogUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjHeroLog.objects.all()
    serializer_class = LogSerializer

# class LogRegister(generics.ListAPIView):
#     queryset = ProjHeroLog.objects.all()
#     serializer_class = LogSerializer


class Login(generics.ListCreateAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        logger.info(request.data)
        if serializer.is_valid():
            data = request.data
            username = data.get('username', None)
            password = data.get('password', None)
            account = auth.authenticate(username=username, password=password)
            if account is not None:
                auth.login(request, account)
                return Response({
                        'msg': 'login successfully',
                        'state': True
                    }, status=status.HTTP_200_OK)
        else:
            logger.info(serializer.errors)
            return Response({'msg': 'parameters invalid', 'state': False}, status=status.HTTP_400_BAD_REQUEST)


