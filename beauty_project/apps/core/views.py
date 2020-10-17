import json

from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from apps.actions.models import Actions


class HomepageView(TemplateView):
    template_name = 'homepage/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Homepage'
        context['actions'] = Actions.objects.filter(active=True).order_by('?')[:4]
        return context


def search_query_view(request):
    print("!!! homepage_search_query_view()")
    print(request)
    if request.method == "POST":
        print("POST request")
        # print(request.POST)
        # print(request.POST.get('city'))
        # print(request.POST.get('date_of_visit'))
        # print(request.POST.get('csrftoken'))

        request_body_json = json.loads(request.body.decode('utf-8'))

        print(request_body_json)
        print(request_body_json['city'])
        print(request_body_json['date_of_visit'])
        print(request_body_json['time_start'])
        print(request_body_json['time_end'])
        print(request_body_json['time_certain_checked'])
        print(request_body_json['time_certain'])
        print(request_body_json['services_added'])

        # import datetime
        # date_time_str = request_body_json['date_of_visit']
        # date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
        # print(date_time_obj)

    return redirect('/')