from permissions.models.users_roles import UserRole
from permissions.models.roles_permissions import RolePermission

def get_roles(employee_number):
    results = {}
    user_roles = UserRole.objects.filter(user__employee_number=employee_number)\
        .select_related('role')
    for user_role in user_roles:
        results[user_role.role.type] = user_role.role.name
    return results

def get_permissions(employee_number):
    results = {}
    try:
        user_roles = UserRole.objects.filter(user__employee_number = employee_number)\
            .select_related('user')
        for user_role in user_roles:
            role_permission = RolePermission.objects.filter(role__id=user_role.role.id).first()
            if role_permission:
                results[role_permission.permission.url] = role_permission.permission.method
    except UserRole.DoesNotExist:
        return None
    return results