from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from users.models import User
from schedules.utils.time import get_today_commute

@api_view(['GET'])
def today_schedule(request):
    employee_number = request.GET.get('employee_number', None)
    try:
        employee = User.objects.get(employee_number=employee_number) 
        work_in, work_out = get_today_commute(employee)
        return Response({
            'name':employee.name,
            'work_in':work_in,
            'work_out':work_out,
        })
    except User.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)