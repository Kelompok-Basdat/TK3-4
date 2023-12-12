from django.urls import path

from reservasi.views import *

app_name = 'reservasi'

urlpatterns = [
    path('add-shuttle/<str:rsv_id>', add_shuttle, name='add_shuttle'),
    path('add-complaint/<str:rsv_id>', add_complaint, name='add_complaint'),
    path('add-review/<str:hname>/<str:hbranch>', add_review, name='add_review'),
    path('add-shuttle-submit', add_shuttle_submit, name='add_shuttle_submit'),
    path('complaint-submit', complaint_submit, name='complaint_submit'),
    path('review-submit', review_submit, name='review_submit'),
]