from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from users.utils.token import validate_login
from users.utils.roles import get_roles
from users.serializers.users import UserSerializer

class Me(APIView):
    @validate_login
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        if not serializer.is_valid:
            return Response("유저 정보가 필요합니다", status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        data["roles"] = get_roles(user.employee_number)
        data["leave"] = user.annual_leave.leave_count
        return Response(data, status=status.HTTP_200_OK)
