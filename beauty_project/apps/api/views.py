# from django.shortcuts import render
from django.http import JsonResponse

from apps.salon.models.salon import Salon
from apps.actions.models import Actions


def api_salons_list_view(request):
    salons = Salon.objects.filter(active=True).values('id', 'name', 'description', 'latitude', 'longitude')
    actions = Actions.objects.filter(active=True)
    actions_salons_ids_list = list(set(actions.values_list('salon__id', flat=True)))

    for salon in salons:
        for action in actions:
            if salon['id'] in actions_salons_ids_list:
                salon['action'] = True
            else:
                salon['action'] = False

    salons_list = list(salons)
    return JsonResponse(salons_list, safe=False)