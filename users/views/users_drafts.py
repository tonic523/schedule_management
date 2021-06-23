import json

from django.utils import timezone

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from users.models import User
from drafts.models.drafts import Draft
from drafts.models.drafts_approers import DraftApprover
from permissions.models.roles import Role
from permissions.models.users_roles import UserRole

class UserDraft(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, id):
        employee = User.objects.get(id=id)
        data= json.loads(request.body)

        APPROVER = UserRole.objects.get(role = Role.objects.get(name="관리자")).user
        
        try:
            draft = Draft.objects.create(
                    drafter = employee,
                    type = data["type"],
                    start_at = data.get("start_at", None),
                    end_at = data.get("end_at", None),
                    description = data.get("description", None),
                    draft_at = timezone.now()
                )
            
            DraftApprover.objects.create(
                approver = APPROVER,
                draft = draft
            )

        except KeyError:
            pass