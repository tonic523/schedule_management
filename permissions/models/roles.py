from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default=None, null=True)

    class Meta:
        db_table = 'roles'