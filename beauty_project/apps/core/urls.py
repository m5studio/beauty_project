from django.urls import path

from apps.core.views import (
    HomepageView,
    homepage_search_query_view,
)

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),

    path('searh-query/', homepage_search_query_view, name='search_query_view'),
]