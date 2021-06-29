from django.db import models

from rest_framework import serializers

from b2tech_intern_20.settings import AUTH_USER_MODEL

class Draft(models.Model):
    TYPE = (
        ('연차', '휴가'),
        ('반차', '휴가'),
        ('공가', '휴가'),
        ('경조', '휴가'),
        ('시차출퇴근제', '근무제도'),
        ('선택근무제', '근무제도'),
        ('재량근무제', '근무제도'),
        ('재택근무제', '근무제도')
    )

    drafter     = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    type        = models.CharField(max_length=64, choices=TYPE)
    description = models.TextField(default=None, null=True)
    draft_at    = models.DateTimeField()
    start_at    = models.DateTimeField(default=None, null=True)
    end_at      = models.DateTimeField(default=None, null=True)
    approval_at = models.DateTimeField(default=None, null=True)
    status      = models.BooleanField(default=False)

    class Meta:
        db_table = 'drafts'
        app_label = 'drafts'