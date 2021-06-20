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
        month, day = month.zfill(2), day.zfill(2) 
        q.add(Q(created_at__date=f'{year}-{month}-{day}'), q.AND)
    
    if employee_number:
        q.add(Q(user__employee_number = employee_number), q.AND)

    schedules = Schedule.objects.filter(q).select_related('user').prefetch_related('user__userrole_set__role')
    results = []
    for schedule in schedules.annotate(
            date = F('created_at__date'),
            attendance_time = F('created_at__time'),
            quitting_time = F('updated_at__time'),
            late_time = F('created_at__time') - F('get_in_time'),
            leaveing_time = F('updated_at__time') - F('get_off_time'),
            work_time = F('updated_at__time') - F('created_at__time')
        ):

        roles = {}
        for userrole in schedule.user.userrole_set.all():
            roles[userrole.role.type] = userrole.role.name

        results.append(
            {
                'employee_number':schedule.user.employee_number,
                'name':schedule.user.name,
                'get_in_time':schedule.get_in_time,
                'get_off_time':schedule.get_off_time,
                'work_type':schedule.work_type,
                'date':schedule.date,
                'created_at' : schedule.attendance_time,
                'updated_at' : schedule.quitting_time,
                'late_time' : schedule.late_time,
                'leaveing_time' : schedule.leaveing_time,
                'work_time' : schedule.work_time,
                'roles' : roles
            }
        )

    return Response({'schedules':results}, status=status.HTTP_200_OK)