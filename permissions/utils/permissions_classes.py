import jwt

from django.utils import timezone
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

from users.models import User
from users.utils.roles import get_roles
from users.utils.token import validate_login
from my_settings import SECRET

class IsLogin(BasePermission):
    @validate_login
    def has_permission(self, request, view):
        return request.user.is_authenticated

class IsAdmin(BasePermission):
    @validate_login
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        roles = get_roles(request.user.employee_number)
        if "관리자" in roles.values():
            return True
        else:
            return False