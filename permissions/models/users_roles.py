from django.db                 import models
from django.db.models.deletion import CASCADE

class UserRole(models.Model):
    user = models.ForeignKey('users.User', on_delete=CASCADE)
    role = models.ForeignKey('permissions.Role', on_delete=CASCADE)

    class Meta:
        db_table = 'roles_by_users'
        app_label = 'permissions'