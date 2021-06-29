from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from users.serializers.users import UserSerializer
from users.utils.roles import get_roles
from users.utils.token import validate_login, is_admin
from users.utils.encrypt_utils import decryption
User = get_user_model()

class UserEmployee(APIView):
    @validate_login
    @is_admin
    def get(self, request, employee_number):
        user = request.user
        if user.employee_number != employee_number:
            return Response("잘못된 접근입니다", status=status.HTTP_401_UNAUTHORIZED)
        user_roles = get_roles(employee_number) #{직책:~~~,부서:~~~,관리자:관리자}
        
        if user_roles.get("관리자", None) == "관리자":
            employees = User.objects.filter()
            employee_list = []
            for employee in employees:
                serializer = UserSerializer(employee)
                information = serializer.data
                information["roles"] = get_roles(employee.employee_number)
                information["registration_number"] = decryption(employee.registration_number)
                employee_list.append(information)               
            return Response({'results':employee_list}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'관리자만 볼 수 있습니다'}, status=status.HTTP_401_UNAUTHORIZED)
