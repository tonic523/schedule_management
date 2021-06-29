from django.db.models import Q, F

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from schedules.models.schedules import Schedule
from schedules.utils.time import work_status, second_to_time, format_time
from users.utils.token import is_admin, validate_login
from b2tech_intern_20.utils import format_list_to_dict

class schedules(APIView):
    @validate_login
    @is_admin
    def get(self, request):
        search = request.GET.get('search', None)
        query = Q()
        if search:
            query.add(Q(user__employee_number__icontains = search), query.OR)
            query.add(Q(user__name__icontains = search), query.OR)

        schedules = Schedule.objects.filter(query)\
            .prefetch_related('user__userrole_set__role')\
            .annotate(
                date = F('created_at__date'),
                attendance_time = F('created_at__time'),
                quitting_time = F('updated_at__time'),
                late_time = F('created_at__time') - F('get_in_time'),
                leaving_time = F('updated_at__time') - F('get_off_time'),
                work_time = F('updated_at__time') - F('created_at__time')
            )
        
        results = [
            {
                'employee_number':schedule.user.employee_number,
                'name':schedule.user.name,
                'get_in_time':format_time(schedule.get_in_time),
                'get_off_time':format_time(schedule.get_off_time),
                'work_type':schedule.work_type,
                'date':schedule.date,
                'work_in' : format_time(schedule.attendance_time),
                'work_out' : format_time(schedule.quitting_time),
                'late_status' : work_status(schedule.created_at,schedule.get_in_time,"지각"),
                'leaving_status' : work_status(schedule.updated_at,schedule.get_off_time,"연장"),
                'leaving_time' : second_to_time(schedule.leaving_time.seconds)
                    if work_status(schedule.updated_at,schedule.get_off_time,"연장") == "연장" else None,
                'work_time' :second_to_time(schedule.work_time.seconds) 
                    if schedule.work_time else None,
                'roles' : format_list_to_dict([
                    {userrole.role.type: userrole.role.name}
                    for userrole in schedule.user.userrole_set.all()])
            }for schedule in schedules]

        return Response({'schedules': results}, status=status.HTTP_200_OK)