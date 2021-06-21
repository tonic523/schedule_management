from django.utils import timezone

# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from schedules.models.schedules import Schedule
from users.models import User

@api_view(['GET'])
@permission_classes([])
def today_schedule(request):
    employee_number = request.GET.get('employee_number', None)
    today_date = timezone.now().strftime('%Y-%m-%d')
    try:
        employee = User.objects.get(employee_number=employee_number)
        try:
            today_schedule = Schedule.objects.get(user=employee, created_at__date = today_date)
            created_at = today_schedule.created_at
            updated_at = today_schedule.updated_at
        except Schedule.DoesNotExist:
            created_at = None
            updated_at = None

        return Response({
            'name':employee.name,
            'created_at':created_at,
            'updated_at':updated_at,
        })

    except User.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)