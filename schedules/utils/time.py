def second_to_time(second):
    print(second)
    if second is None:
        return None
    else:
        hour, miniute = second // 3600, second % 3600
        miniute = miniute // 60
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