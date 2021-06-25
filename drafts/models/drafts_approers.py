from django.db import models

from b2tech_intern_20.settings import AUTH_USER_MODEL
from .drafts import Draft
class DraftApprover(models.Model):
    approver = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    draft    = models.ForeignKey(Draft, on_delete=models.CASCADE)
    status   = models.BooleanField(default=False)

    class Meta:
        db_table = 'drafts_approvers'
        app_label = 'drafts'