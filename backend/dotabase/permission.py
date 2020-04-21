from rest_framework import permissions
from django.contrib.auth.models import User
import logging

logger = logging.getLogger('django')

class AdminCheck(permissions.BasePermission):
    def has_permission(self, request, view):
        logger.info(request.user)
        if request.method in permissions.SAFE_METHODS:
            logger.info("just get")
            return True
        logger.info("not safe")
        return not request.user.is_anonymous
