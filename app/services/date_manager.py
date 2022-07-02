from datetime import datetime


def get_current_date() -> str:
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')
