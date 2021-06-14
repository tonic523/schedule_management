from django.db import models

class Permission(models.Model):
    url    = models.CharField(max_length=128)
    method = models.CharField(max_length=16)

    class Meta:
        db_table = 'permissions'
        app_label = 'permissions'