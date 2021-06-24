def format_str_date(date):
    year, month, day = date.split('-')
    month, day = month.zfill(2), day.zfill(2)
    return  f'{year}-{month}-{day}'
            