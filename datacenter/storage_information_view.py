from datacenter.models import Visit
from django.shortcuts import render
from datacenter.helper_functions import get_duration, format_duration
from django.utils.timezone import localtime


def storage_information_view(request):

    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for visit in visits:
        duration = get_duration(visit)
        spented_time = format_duration(duration)

        who_entered = visit.passcard
        entered_at = localtime(visit.entered_at)

        non_closed_visits.append(
            {
                'who_entered': who_entered,
                'entered_at': entered_at,
                'duration': spented_time,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
