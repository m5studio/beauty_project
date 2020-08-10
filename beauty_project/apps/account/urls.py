from django.urls import path, include

from apps.account.views import (
    logout_view,
    registration_view,
    login_view,

    user_profile_view,
    change_password_view,
    reset_password_view,

    add_salon_client_view,
    add_salon_action_view,

    register_by_phone_view,
    register_password_view,
)


app_name = 'user'

urlpatterns = [
    path('user/', include([
        # path('register/', registration_view, name='registration'),

        path('login/', login_view, name='login'),
        path('logout/', logout_view, name='logout'),

        path('reset-password/', reset_password_view, name='reset-password'),

        path('registration/', register_by_phone_view, name='registration-by-phone'),
        path('registration/password/', register_password_view, name='registration-password'),
    ])),

    path('profile/', include([
        path('', user_profile_view, name='profile'),
        path('change-password/', change_password_view, name='change-password'),

        path('salon/add-client/', add_salon_client_view, name='add-salon-client'),
        path('salon/add-action/', add_salon_action_view, name='add-salon-action'),
    ])),
]