from django.urls import path, include

from apps.api.views import (
    api_salons_list_view,
)


app_name = 'api'

urlpatterns = [
    path('api/', include([
        path('salons/', api_salons_list_view, name='salons'),
    ])),
]