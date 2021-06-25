from django.db                 import models
from django.db.models.deletion import CASCADE

from b2tech_intern_20.settings import AUTH_USER_MODEL
from .roles import Role
class UserRole(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=CASCADE)
    role = models.ForeignKey(Role, on_delete=CASCADE)

    class Meta:
        db_table = 'roles_by_users'
        app_label = 'permissions'