from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView

from users.utils.token import validate_login
from users.utils.roles import get_roles
from users.serializers.login import UserSerializer
class Me(APIView):
    permission_classes = []
    @validate_login
    def get(self, request):
        employee = request.user
        serializer = UserSerializer(employee)
        # data = {
        #     'name':employee.name,
        #     'employee_number':employee.employee_number,
        #     'roles':get_roles(employee.employee_number),
        #     'remaining_annual_leave':employee.remaining_annual_leave
        # }
        return Response(serializer.data, status=status.HTTP_200_OK)