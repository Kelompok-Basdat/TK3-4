from django.urls import path

from Han.views import *

app_name = 'Han'

urlpatterns = [
    path('daftar_kamar', daftar_kamar, name='daftar_kamar'),
    path('daftar_reservasi', daftar_reservasi, name='daftar_reservasi'),
    path('create_kamar', create_kamar, name='create_kamar'),
    path('detail_reservasi/<str:rsv_id>', detail_reservasi, name='detail_reservasi'),
]