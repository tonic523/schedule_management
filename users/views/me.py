from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from users.utils.token import validate_login
from users.serializers.users import UserSerializer
class Me(APIView):
    permission_classes = []
    @validate_login
    def get(self, request):
        employee = request.user
        serializer = UserSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
