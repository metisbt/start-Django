from django.urls import path
from maintenance.views import *

app_name = 'maintenance'

urlpatterns = [
    path('', maintenance, name='maintenance'),
]