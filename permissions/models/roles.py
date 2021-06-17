from django.db import models

class Role(models.Model):
    type = models.CharField(max_length=64, default=None, null=True)
    name = models.CharField(max_length=128, default=None, null=True)
    
    class Meta:
        db_table = 'roles'
        app_label = 'permissions'