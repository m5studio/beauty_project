# from django.shortcuts import render
from django.http import JsonResponse

from apps.salon.models.salon import Salon
from apps.salon.models.work_schedule import WorkSchedule
from apps.actions.models import Actions

import datetime


def api_salons_list_view(request):
    salons = Salon.objects.filter(active=True).values('id', 'name', 'description', 'latitude', 'longitude')
    actions = Actions.objects.filter(active=True)
    actions_salons_ids_list = list(set(actions.values_list('salon__id', flat=True)))

    today_weekday = datetime.datetime.today().weekday()

    for salon in salons:
        # salon_instance = Salon.objects.get(id=salon['id'])

        # Actions
        for action in actions:
            if salon['id'] in actions_salons_ids_list:
                salon['action'] = True
            else:
                salon['action'] = False
        '''
        # Get current day Working schedule
        salon_ws = WorkSchedule.objects.filter(salon=salon['id'])
        for ws in salon_ws:
            # print(f'{ws.get_week_day_display()} ({ws.week_day})')
            # print(f'from: {ws.working_hours_from}')
            # print(f'to: {ws.working_hours_to}')

            if int(ws.week_day) == int(today_weekday):
                today_ws = WorkSchedule.objects.get(salon=salon['id'], week_day=today_weekday)
                # today_ws = WorkSchedule.objects.filter(salon=salon['id'], week_day=today_weekday).first()
                print(today_ws.working_hours_from)
                print(today_ws.working_hours_to)

        print('\n')
        '''


    salons_list = list(salons)
    return JsonResponse(salons_list, safe=False)