from django.db import models

class Schedule(models.Model):
    TYPE = (
        ('유급휴가', 8),
        ('무급휴가', 0),
        ('정상근무', 8),
    )
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    work_type  = models.CharField(max_length=64, choices=TYPE, default='정상근무')
    created_at = models.DateTimeField(null=True, default=None)
    updated_at = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'schedules'
        app_label = 'schedules'