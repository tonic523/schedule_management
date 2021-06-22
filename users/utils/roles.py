from permissions.models.users_roles import UserRole

def get_roles(employee_number):
    results = {}
    user_roles = UserRole.objects.filter(user__employee_number=employee_number).select_related('role')
    for user_role in user_roles:
        user_role.role.type = user_role.role.name
    return results