import datetime

# from django.shortcuts import render
from django.http import JsonResponse

from apps.salon.models.salon import Salon
from apps.salon.models.work_schedule import WorkSchedule
from apps.salon.models.address import Address

from apps.actions.models import Actions


def api_salons_list_view(request):
    # salons = Salon.objects.filter(active=True).values('id', 'name', 'description', 'latitude', 'longitude')
    salons = Salon.objects.filter(active=True).values('id', 'name', 'description')

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

        #  Addresses
        salon['addresses'] = []
        salons_addresses = list(Address.objects.filter(salon__id=salon['id']).values('city__name', 'metro__name', 'street', 'building', 'latitude', 'longitude'))

        for salon_address in salons_addresses:

            # Working schedule for address
            salon_address['working_schedule'] = {}
            address_working_schedules = WorkSchedule.objects.filter(address__salon__id=salon['id'], week_day=today_weekday)
            for aws in address_working_schedules:
                if int(aws.week_day) == int(today_weekday):

                    # Compare current time and Salon working_hours_to
                    if int(str(now_time).replace(':','')) < int(str(aws.working_hours_to).replace(':','')):
                        salon_address['working_schedule']['open_now'] = True
                    else:
                        salon_address['working_schedule']['open_now'] = False

                    salon_address['working_schedule']['open_from'] = aws.working_hours_from
                    salon_address['working_schedule']['open_to'] = aws.working_hours_to

            salon['addresses'].append(salon_address)

        # Get current day Working schedule
        # salon['working_schedule'] = {}
        # salon['working_schedule']['open_now'] = False

        # salon_ws = WorkSchedule.objects.filter(address__salon=salon['id'])
        # for ws in salon_ws:
        #     if int(ws.week_day) == int(today_weekday):
        #         today_ws = WorkSchedule.objects.get(address__salon=salon['id'], week_day=today_weekday)

        #         # Compare current time and Salon working_hours_to
        #         if int(str(now_time).replace(':','')) < int(str(today_ws.working_hours_to).replace(':','')):
        #             salon['working_schedule']['open_now'] = True

        #         salon['working_schedule']['open_from'] = today_ws.working_hours_from
        #         salon['working_schedule']['open_to'] = today_ws.working_hours_to

    salons_list = list(salons)
    return JsonResponse(salons_list, safe=False)