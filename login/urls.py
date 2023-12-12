from django.urls import path

from login.views import *

app_name = 'login'

urlpatterns = [
    path('', show_landingpage, name='show_landingpage'),
    path('login/', login_user, name='login'),
    path('login-submit/', login, name='login_submit'),
    path('logout_user', logout_user, name='logout'),
]