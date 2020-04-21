from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

router = DefaultRouter()

urlpatterns = [
    url(r'^hero/$', HeroList.as_view()),
    url(r'^hero/(?P<pk>[0-9]+)/$', HeroUpdate.as_view()),
    #url(r'^user/$', UserRegister.as_view()),
    url(r'^log/$', LogRegister.as_view()),
    url(r'^user/login/$', Login.as_view()),
    url(r'^user/get_token/$', obtain_jwt_token),
    url(r'^user/token_validate/$', verify_jwt_token),
]