from django.urls import path

from reservasi.views import add_complaint, add_review, add_shuttle

app_name = 'reservasi'

urlpatterns = [
    path('add-shuttle', add_shuttle, name='add_shuttle'),
    path('add-complaint', add_complaint, name='add_complaint'),
    path('add-review', add_review, name='add_review'),
]