from django.utils import timezone

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from drafts.models.drafts import Draft
from drafts.models.drafts_approers import DraftApprover
from permissions.models.roles import Role
from permissions.models.users_roles import UserRole
from users.utils.token import validate_login
class UserDraft(APIView):
    permission_classes = []

    @validate_login
    def post(self, request, id):
        employee = request.user
        data= request.data

        ADMIN = UserRole.objects.get(role = Role.objects.get(name="관리자")).user
        approvers = [ADMIN]
        
        try:
            draft = Draft.objects.create(
                    drafter = employee,
                    type = data["type"],
                    start_at = data.get("start_at", None),
                    end_at = data.get("end_at", None),
                    description = data.get("description", None),
                    draft_at = timezone.now()
                )
        except KeyError:
            return Response({'message':'기안 유형을 입력해주세요'}, status=status.HTTP_400_BAD_REQUEST) 

        for apporver in approvers:
            DraftApprover.objects.create(
                approver = apporver,
                draft = draft
            )
        return Response({'message':'SUCCESS'}, status=status.HTTP_201_CREATED)