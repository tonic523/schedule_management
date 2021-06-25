from schedules.models.schedules import Schedule
from django.utils import timezone

def second_to_time(second):
    if second is None:
        return None
    else:
        hour, miniute = str(second // 3600).zfill(2), second % 3600
        miniute = str(miniute // 60).zfill(2)
        return f'{hour}:{miniute}'

def work_status(time, status):
    if time is None:
        return None
    elif status == '지각':
        return status if time.days > 0 else None
    elif status == '연장':
        return status if time.seconds > 0 else None
        

def get_worktime(time):
    if time is None:
        return None
    else:
        return time.seconds if time.seconds > 0 else None

def format_time(time):
    FORMAT = '%H:%M'
    return time.strftime(FORMAT) if time else None

def get_today_commute(employee):
    try:
        today_schedule = Schedule.objects.get(user=employee, created_at__date = timezone.now().strftime('%Y-%m-%d'))
        created_at = today_schedule.created_at
        updated_at = today_schedule.updated_at
    except Schedule.DoesNotExist:
        created_at = None
        updated_at = None
    return created_at, updated_at