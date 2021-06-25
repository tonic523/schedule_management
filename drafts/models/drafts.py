from django.db import models

from rest_framework import serializers

from b2tech_intern_20.settings import AUTH_USER_MODEL

class Draft(models.Model):
    TYPE = (
        ('연차', 1),
        ('반차', 0.5),
        ('공가', 0),
        ('경조', 0)
    )

    drafter     = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    type        = models.CharField(max_length=64, choices=TYPE)
    description = models.TextField()
    draft_at    = models.DateField()
    start_at    = models.DateField(default=None, null=True)
    end_at      = models.DateField(default=None, null=True)
    approval_at = models.DateField(default=None, null=True)
    status      = models.BooleanField(default=False)

    class Meta:
        db_table = 'drafts'
        app_label = 'drafts'

class DraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draft
        fields = ['']
