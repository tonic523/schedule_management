from django.db import models

from users.models import User
from .drafts      import Draft

class DraftApprover(models.Model):
    approver = models.ForeignKey(User, on_delete=models.CASCADE)
    draft    = models.ForeignKey(Draft, on_delete=models.CASCADE)
    status   = models.BooleanField(default=False)

    class Meta:
        db_table = 'drafts_approvers'