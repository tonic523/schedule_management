from django.utils              import timezone
from django.db                 import models
from django.db.models.deletion import CASCADE

class Work(models.Model):
    STATUS = (
        (1, "출근 전"),
        (2, "출근"),
        (3, "지각"),
        (4, "결석"),
        (5, "퇴근"),
        (6, "야근"),
        (7, "휴일근무")
        )
    user      = models.ForeignKey('users.User', on_delete=CASCADE)
    status    = models.IntegerField(default=1, choices=STATUS)
    start_at  = models.DateTimeField(default=timezone.now())
    end_at    = models.DateTimeField(default=None, null=True)
    
    class Meta:
        db_table = 'schedules'

class Leave(models.Model):
    STATUS = (
        (1, "신청"),
        (2, "결재"),
        (3, "반려")
        )
    LEAVE_TYPE = (
        ("연차", 1),
        ("공가", 0),
        ("경조", 0)
        )
    user     = models.ForeignKey('users.User', on_delete=CASCADE)
    start_at = models.DateTimeField()
    end_at   = models.DateTimeField()
    status   = models.IntegerField(default=1, choices=STATUS)
    text     = models.TextField()
    type     = models.CharField(default="연차", choices=LEAVE_TYPE, max_length=32)

    class Meta:
        db_table = 'leaves'