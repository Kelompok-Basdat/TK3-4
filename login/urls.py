from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.show_landingpage, name='show_landingpage'),
    path('login/', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
]