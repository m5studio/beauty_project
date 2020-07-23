from django.urls import path

from apps.core.views import HomepageView
from apps.core.views import ProfileView


urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),

    path('accounts/profile/', ProfileView.as_view(), name="account_profile")
]