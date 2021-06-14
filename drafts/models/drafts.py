from django.db import models

from .drafts_approers import DraftApprover

class Draft(models.Model):
    TYPE = (
        ('연차', 1),
        ('반차', 0.5),
        ('공가', 0),
        ('경조', 0)
    )

    drafter     = models.ForeignKey('users.User', on_delete=models.CASCADE)
    approvers   = models.ManyToManyField('users.User', through=DraftApprover, related_name='drafts')
    type        = models.CharField(max_length=64)
    description = models.TextField()
    draft_at    = models.DateField()
    start_at    = models.DateField(default=None, null=True)
    end_at      = models.DateField(default=None, null=True)
    approval_at = models.DateField(default=None, null=True)
    status      = models.BooleanField(default=False)

    class Meta:
        db_table = 'drafts'
        app_label = 'drafts'