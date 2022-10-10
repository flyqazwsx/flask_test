def get_date():
    from datetime import datetime
    date = datetime.now()

    return date.strftime('%Y-%m-%d %H:%M:%S')
