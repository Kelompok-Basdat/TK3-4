from django.urls import path
from hotel.views import *

app_name = 'hotel'

urlpatterns = [
    path('search', find_hotel, name='find_hotel'),
    path('1', specific_hotel, name='specific_hotel'),
    path('fasilitas/<str:hotel_name>/<str:hotel_branch>/', fasilitas_hotel, name='fasilitas_hotel'),
    path('fasilitas/<str:hotel_name>/<str:hotel_branch>/create', create_fasilitas_hotel, name='create_fasilitas_hotel'),
    path('fasilitas/<str:hotel_name>/<str:hotel_branch>/<str:facilities>', update_fasilitas_hotel, name='update_fasiltias_hotel'),
    path('fasilitas/<str:hotel_name>/<str:hotel_branch>/<str:facilities>/delete', delete_fasilitas_hotel, name='delete_fasiltias_hotel'),
]