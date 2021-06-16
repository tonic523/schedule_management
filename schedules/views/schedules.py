from django.db.models import Q

# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from schedules.models.schedules import Schedule

@api_view(['GET'])
@permission_classes([])
def scheduleList(request):
    if request.method == 'GET':
        employee_number = request.GET.get('employee_number', None)
        date = request.GET.get('date', None)

        q = Q()
        if date:
            year, month, day = date.split('-')
            if len(month) < 2:
                month = '0' + month
            if len(day) < 2:
                day = '0' + day
            q.add(Q(created_at__year=year), q.AND)
            q.add(Q(created_at__month=month), q.AND)
            q.add(Q(created_at__day=day), q.AND)
        
        if employee_number:
            q.add(Q(user__employee_number = employee_number), q.AND)

        schedules = Schedule.objects.filter(q)
        
        return Response({'schedules':[
            {
            'employee_number':schedule.user.employee_number,
            'name':schedule.user.name,
            'created_at' : schedule.created_at,
            'updated_at' : schedule.updated_at
            }for schedule in schedules]
        }, status=status.HTTP_200_OK)