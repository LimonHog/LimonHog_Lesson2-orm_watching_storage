from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.helper_functions import is_visit_long, get_duration
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for passcard_visit in passcard_visits:
        duration = get_duration(passcard_visit)
        is_strange = is_visit_long(duration)

        this_passcard_visits.append(
            {
                'entered_at': passcard_visit.entered_at,
                'duration': duration,
                'is_strange': is_strange
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
