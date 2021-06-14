from django.db                 import models
from django.db.models.deletion import CASCADE

from .permissions import Permission

class RolePermission(models.Model):
    permission = models.ForeignKey(Permission, on_delete=CASCADE)
    role       = models.ForeignKey('permissions.Role', on_delete=CASCADE)

    class Meta:
        db_table = 'permissions_by_roles'
        app_label = 'permissions'