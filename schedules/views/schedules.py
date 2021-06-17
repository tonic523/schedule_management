from django.db.models import Q, F

# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from schedules.models.schedules import Schedule

@api_view(['GET'])
@permission_classes([])
def scheduleList(request):
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

    schedules = Schedule.objects.filter(q).select_related('user').prefetch_related('user__userrole_set__role')
    
    return Response({'schedules':[
        {
        'employee_number':schedule.user.employee_number,
        'name':schedule.user.name,
        'role':[{
            userrole.role.type : userrole.role.name
            }for userrole in schedule.user.userrole_set.all()],
        'get_in_time':schedule.get_in_time,
        'get_off_time':schedule.get_off_time,
        'work_type':schedule.work_type,
        'created_at' : schedule.created_at,
        'updated_at' : schedule.updated_at,
        'late_time' : schedule.late_time,
        'leaveing_time' : schedule.leaveing_time,
        'work_time' : schedule.work_time
        }for schedule in schedules.annotate(
            late_time = F('created_at__time') - F('get_in_time'),
            leaveing_time = F('updated_at__time') - F('get_off_time'),
            work_time = F('updated_at__time') - F('created_at__time')
        )]
    }, status=status.HTTP_200_OK)