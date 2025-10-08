from django.utils.timezone import localtime
from datetime import datetime, timezone


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    if visit.leaved_at :
        leaved_at = localtime(visit.leaved_at)
        delta = leaved_at - entered_at
    else:
        date_now = localtime(datetime.now(timezone.utc))
        delta = date_now - entered_at

    return delta


def format_duration(duration):
    total_seconds = duration.total_seconds()

    minutes_in_hour = 60
    seconds_in_hour = 3600
    seconds_in_minute = 60

    hours = total_seconds // seconds_in_hour
    minutes = (total_seconds % seconds_in_hour) // minutes_in_hour
    seconds = total_seconds % seconds_in_minute
    inside_duration = "%02d:%02d:%02d" % (hours, minutes, seconds)

    return inside_duration


def is_visit_long(duration, minutes=60):
    minutes_in_hour = 60
    total_seconds = minutes * minutes_in_hour
    long_visit = duration.total_seconds() > total_seconds

    return long_visit
