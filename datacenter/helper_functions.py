from django.utils.timezone import localtime
from datetime import datetime, timezone



def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    if visit.leaved_at == None:
        date_now = localtime(datetime.now(timezone.utc))
        delta = date_now - entered_at
    else:
        leaved_at = localtime(visit.leaved_at)
        delta = leaved_at - entered_at

    return delta


def format_duration(duration):
    
    total_seconds = duration.total_seconds()

    hours = total_seconds // 3600
    minutes = (total_seconds%3600) // 60
    seconds = total_seconds%60
    inside_duration = "%02d:%02d:%02d" % (hours, minutes, seconds)

    return inside_duration


def is_visit_long(duration, minutes=60):

    total_seconds = minutes * 60
    long_visit = duration.total_seconds() > total_seconds

    return long_visit