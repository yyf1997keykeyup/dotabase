from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

router = DefaultRouter()

urlpatterns = [
    url(r'^hero/$', HeroList.as_view()),
    url(r'^hero/(?P<pk>[0-9]+)/$', HeroUpdate.as_view()),
    #url(r'^user/$', UserRegister.as_view()),
    url(r'^hero_log/$', LogList.as_view()),
    url(r'^hero_log/(?P<pk>[0-9]+)/$', LogUpdate.as_view()),
    url(r'^item/$', ItemList.as_view()),
    url(r'^item/(?P<pk>[0-9]+)/$', ItemUpdate.as_view()),
    url(r'^hero_good_against/$',HeroGoodAgainst.as_view()),
    url(r'^hero_bad_against/$',HeroBadAgainst.as_view()),
    url(r'^hero_best_combos/$',HeroBestCombos.as_view()),
    url(r'^hero_skill/$',Skill.as_view()),
    url(r'^hero_skill/(?P<pk>[0-9]+)/$',SkillUpdate.as_view()),
    url(r'^hero_hero_skill/$',HeroSkill.as_view()),
    url(r'^hero_hero_skill/(?P<pk>[0-9]+)/$',HeroSkillUpdate.as_view()),
    url(r'^user/login/$', Login.as_view()),
    url(r'^user/get_token/$', obtain_jwt_token),
    url(r'^user/token_validate/$', verify_jwt_token),
]