from django.urls import path

from cr_pengguna.views import *

app_name = 'cr_pengguna'

urlpatterns = [
    path('', register, name='register'),
    path('user/', register_user, name='register_user'),
    path('hotel/', register_hotel, name='register_hotel'),
]