from django.utils import timezone

from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView

from drafts.models.drafts import Draft
from drafts.models.drafts_approers import DraftApprover
from permissions.models.roles import Role
from permissions.models.users_roles import UserRole

from drafts.serializers.drafts import DraftSerializer

from users.utils.token import validate_login

class UserDraft(APIView):
    permission_classes = []
    @validate_login
    def post(self, request, employee_number):
        user = request.user
        if user.employee_number != employee_number:
            return Response("잘못된 접근입니다", status=status.HTTP_401_UNAUTHORIZED)
        
        data= request.data
        ADMIN = UserRole.objects.get(role = Role.objects.get(name="관리자")).user
        approvers = [ADMIN]
        
        try:
            draft = Draft.objects.create(
                    drafter = user,
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
    
    @validate_login
    def get(self, request, employee_number):
        user = request.user
        if user.employee_number != employee_number:
            return Response("잘못된 접근입니다", status=status.HTTP_401_UNAUTHORIZED)
        
        drafts = Draft.objects.filter(drafter=user)\
            .select_related('drafter')
        
        serializer = DraftSerializer(drafts, many=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)