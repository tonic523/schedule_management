from permissions.models.roles import Role
from permissions.models import roles_permissions
from permissions.models.users_roles import UserRole
from permissions.models.roles_permissions import RolePermission
from rest_framework.permissions import BasePermission
from rest_framework_jwt.utils import 
def get_roles(employee_number):
    results = {}
    user_roles = UserRole.objects.filter(user__employee_number=employee_number).select_related('role')
    for user_role in user_roles:
        user_role.role.type = user_role.role.name
    return results

def get_permissions(employee_number):
    results = []
    roles = get_roles(employee_number)
    role_permissions = RolePermission.objects.filter(role__in=roles).select_related('role', 'permission')
    for role_permission in role_permissions:
        results.append((role_permission.permission.method, role_permission.permission.url))
    return results

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        access_token = request.headers['Authorization']
        return request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        permissions = get_permissions(request.user.employee_number)
        return True