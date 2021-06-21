from permissions.models.users_roles import UserRole

def get_roles(employee_number):
    results = {}
    roles = UserRole.objects.filter(user__employee_number=employee_number).select_related('role')
    for role in roles:
        role.type = role.name
    return results