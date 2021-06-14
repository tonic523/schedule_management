from django.db import models

class Permission(models.Model):
    url    = models.CharField(max_length=128)
    method = models.CharField(max_length=128)

    class Meta:
        db_table = 'rights'