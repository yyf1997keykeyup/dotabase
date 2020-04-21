import django_filters
from register.models import *

class UserFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(field_name="username")
    password = django_filters.CharFilter(field_name="password")

    class Meta:
        model = AuthUser
        fields = ['username', 'password',]