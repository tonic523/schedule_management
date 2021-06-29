from datetime import timedelta

from django.utils import timezone
from django.db.models import F, Sum

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from users.utils.token import validate_login
from schedules.utils.time import second_to_time, get_today_commute
from users.utils.roles import get_roles

class MyPage(APIView):
    @validate_login
    def get(self, request, employee_number):
        employee = request.user
        if employee_number != employee.employee_number:
            return Response({'message':'잘못된 접근 입니다'}, status=status.HTTP_401_UNAUTHORIZED)

        work_in, work_out = get_today_commute(employee)
        today = timezone.now()

        # 일주일 날짜 리스트
        sunday = today - timedelta(days=today.isoweekday() % 7 - 1)
        weekdays = []
        for i in range(7):
            weekdays.append(sunday + timedelta(days=i))

        # 날짜 별 일한 시간 , 총 일한 시간
        work_time_list = {}
        total_work_time = None
        schedules = employee.schedule_set.filter(created_at__date__range=[weekdays[0], weekdays[6]])\
            .annotate(
                work_time = F('updated_at__time') - F('created_at__time')
            )
        try:
            total_work_time = second_to_time(
                schedules.aggregate(Sum('work_time', distinct=True))['work_time__sum'].seconds)
        except AttributeError:
            pass

        # 일하지 않은 날짜는 None
        for weekday in weekdays:
            for idx, schedule in enumerate(schedules):
                work_time_list[weekday] = None
                if not schedule.updated_at:
                    pass
                elif weekday.strftime("%Y-%m-%d") != schedule.updated_at.strftime("%Y-%m-%d"):
                    pass
                else:
                    work_time_list[weekday] = second_to_time(schedule.work_time.seconds)
                    break    
        
        data = {
            'name':employee.name,
            'employee_number':employee.employee_number,
            'roles':get_roles(employee.employee_number),
            'work_in':work_in,
            'work_out':work_out,
            'work_time_list':list(work_time_list.values()),
            'total_work_in_week':total_work_time
            }
        return Response(data, status=status.HTTP_200_OK)