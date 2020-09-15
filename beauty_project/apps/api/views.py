# from django.shortcuts import render
from django.http import JsonResponse

from apps.salon.models.salon import Salon


def api_salons_list_view(request):
    salons = Salon.objects.filter(active=True).values('id', 'name', 'description', 'latitude', 'longitude')
    salons_list = list(salons)
    return JsonResponse(salons_list, safe=False)