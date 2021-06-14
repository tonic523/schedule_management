from django.db import models

from users.models import User

class Schedule(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    type       = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'schedules'