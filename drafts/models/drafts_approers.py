from django.db import models

class DraftApprover(models.Model):
    approver = models.ForeignKey('users.User', on_delete=models.CASCADE)
    draft    = models.ForeignKey('drafts.Draft', on_delete=models.CASCADE)
    status   = models.BooleanField(default=False)

    class Meta:
        db_table = 'drafts_approvers'
        app_label = 'drafts'