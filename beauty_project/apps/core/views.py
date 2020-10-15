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


def homepage_search_query_view(request):
    print("!!! homepage_search_query_view()")
    print(request)
    return redirect('/')