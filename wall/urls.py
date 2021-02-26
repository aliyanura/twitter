from django.urls import path
from .views import *

urlpatterns = [
    path('wall/', Wall, name='wall'),
]