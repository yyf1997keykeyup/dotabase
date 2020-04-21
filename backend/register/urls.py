from django.conf.urls import url, include
from rest_framework import routers
from register.views import *


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^user/$', UserRegister.as_view()),
]