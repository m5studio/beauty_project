from django.urls import path, include

from apps.account.views import (
    logout_view,
    registration_view,
    login_view,

    personal_cabinet_view,

    register_by_phone_view,
    register_password_view,
)


app_name = 'user'

urlpatterns = [
    path('user/', include([
        path('register/', registration_view, name='registration'),
        path('login/', login_view, name="login"),
        path('logout/', logout_view, name="logout"),

        path('cabinet/', personal_cabinet_view, name="cabinet"),

        path('register-by-phone/', register_by_phone_view, name='registration-by-phone'),
        path('register-password/', register_password_view, name='registration-password'),
    ]))
]