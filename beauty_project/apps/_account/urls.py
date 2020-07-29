from django.urls import path

from apps.account.views import (
    logout_view,
    registration_view,
    registration_phone_view,
)


urlpatterns = [
    path('logout/', logout_view, name="logout"),
    path('register/', registration_view, name='registration'),
    path('registration-phone/', registration_phone_view, name='registration-phone'),
]