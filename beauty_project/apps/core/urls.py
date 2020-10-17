from django.urls import path, include

from apps.core.views import (
    HomepageView,

    search_query_view,
)


search_patterns = ([
    path('searh-query/', search_query_view, name='query_view'),
], 'search')

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),

    # path('searh-query/', search_query_view, name='search_query_view'),
    path('core/', include(search_patterns)),
]