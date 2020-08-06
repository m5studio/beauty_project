from django.urls import path, include

from apps.account.views import (
    logout_view,
    registration_view,
    login_view,

    user_profile_view,
    change_password_view,
    reset_password_view,

    add_salon_client_view,

    register_by_phone_view,
    register_password_view,
)


app_name = 'user'

urlpatterns = [
    path('user/', include([
        path('register/', registration_view, name='registration'),
        path('login/', login_view, name='login'),
        path('logout/', logout_view, name='logout'),

        path('profile/', user_profile_view, name='profile'),
        path('profile/change-password/', change_password_view, name='change-password'),
        path('reset-password/', reset_password_view, name='reset-password'),

        path('profile/salon/add-client/', add_salon_client_view, name='add-salon-client'),

        path('register-by-phone/', register_by_phone_view, name='registration-by-phone'),
        path('register-password/', register_password_view, name='registration-password'),
    ]))
]