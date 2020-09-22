import datetime

# from django.shortcuts import render
from django.http import JsonResponse

from apps.salon.models.salon import Salon
from apps.salon.models.work_schedule import WorkSchedule
from apps.actions.models import Actions


def api_salons_list_view(request):
    salons = Salon.objects.filter(active=True).values('id', 'name', 'description', 'latitude', 'longitude')
    actions = Actions.objects.filter(active=True)
    actions_salons_ids_list = list(set(actions.values_list('salon__id', flat=True)))

    now = datetime.datetime.now()
    today_weekday = datetime.datetime.today().weekday()
    now_time = f'{now.hour}:{now.minute}:{now.second}'

    for salon in salons:
        # Actions
        for action in actions:
            if salon['id'] in actions_salons_ids_list:
                salon['has_actions'] = True
            else:
                salon['has_actions'] = False

        # Get current day Working schedule
        salon['working_schedule'] = {}
        salon['working_schedule']['open_now'] = False

        salon_ws = WorkSchedule.objects.filter(salon=salon['id'])
        for ws in salon_ws:
            if int(ws.week_day) == int(today_weekday):
                today_ws = WorkSchedule.objects.get(salon=salon['id'], week_day=today_weekday)

                # Compare current time and Salon working_hours_to
                if int(str(now_time).replace(':','')) < int(str(today_ws.working_hours_to).replace(':','')):
                    salon['working_schedule']['open_now'] = True

                salon['working_schedule']['open_from'] = today_ws.working_hours_from
                salon['working_schedule']['open_to'] = today_ws.working_hours_to

    salons_list = list(salons)
    return JsonResponse(salons_list, safe=False)