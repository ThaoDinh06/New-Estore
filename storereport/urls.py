from django.urls import path
from storereport.views import *


app_name = 'storereport'
urlpatterns = [
    path('report/', html_to_pdf, name='report'),
]
