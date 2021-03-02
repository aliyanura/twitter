from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('wall/<int:pk>/', wall_posts, name='wall_posts'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('follow/<int:pk>/', follow, name='follow'),
]