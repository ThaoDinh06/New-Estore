from django.urls import path
from analysis.views import *


app_name = 'analysis'
urlpatterns = [
    path('chart/', work_with_chart, name='work_with_chart'),
]
