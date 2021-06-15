from django.db import models

class Schedule(models.Model):
    TYPE = (
        ('유급휴가', 8),
        ('무급휴가', 0),
        ('정상근무', 8),
    )
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    type       = models.CharField(max_length=64, choices=TYPE, default='정상근무')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'schedules'
        app_label = 'schedules'