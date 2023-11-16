from django.urls import path
from hotel.views import *

app_name = 'hotel'

urlpatterns = [
    path('search', find_hotel, name='find_hotel'),
    path('1', specific_hotel, name='specific_hotel'),
    path('fasilitas', fasilitas_hotel, name='fasilitas_hotel'),
    path('fasilitas/create', create_fasilitas_hotel, name='create_fasilitas_hotel'),
    path('fasilitas/update', update_fasilitas_hotel, name='update_fasiltias_hotel'),
]