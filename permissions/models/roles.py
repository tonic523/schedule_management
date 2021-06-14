from django.db import models
from django.db.models.deletion import CASCADE

class Role(models.Model):
    name        = models.CharField(max_length=128)
    description = models.TextField(default=None, null=True)
    
    class Meta:
        db_table = 'roles'
        app_label = 'permissions'