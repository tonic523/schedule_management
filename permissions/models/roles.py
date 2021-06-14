from django.db import models

from .roles_permissions import RolePermission

class Role(models.Model):
    name        = models.CharField(max_length=128)
    description = models.TextField(default=None, null=True)
    permissions = models.ManyToManyField('permissions.Permission', through=RolePermission, related_name="roles")
    
    class Meta:
        db_table = 'roles'