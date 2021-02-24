from django.urls import path
from .views import *

urlpatterns = [
    path('wall/', WallListView.as_view(), name='wall'),
]