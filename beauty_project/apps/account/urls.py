from django.urls import path, include

from apps.account.views import (
    logout_view,
    registration_view,
    login_view,
)


app_name = 'user'

urlpatterns = [
    path('user/', include([
        path('register/', registration_view, name='registration'),
        path('login/', login_view, name="login"),
        path('logout/', logout_view, name="logout"),
    ]))
]