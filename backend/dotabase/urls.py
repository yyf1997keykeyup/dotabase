from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

urlpatterns = [
    url(r'^hero/$', HeroList.as_view()),
    url(r'^hero/(?P<pk>[0-9]+)/$', HeroUpdate.as_view()),
    url(r'^user/$', UserRegister.as_view()),
    url(r'^herolog/$', LogRegister.as_view()),
]