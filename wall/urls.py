from django.urls import path
from .views import *

urlpatterns = [
    path('wall/', Wall, name='wall'),
    path('wall/search/', search, name='search'),
    path('account/<int:pk>/foto/<int:image_pk>/', change_foto, name='change_foto'),
    path('account/<int:pk>/foto/add/', add_foto, name='add_foto'),
    path('wall/<int:pk>/post/add/',  post_add, name='post_add'),
    path('wall/<int:pk>/post/<int:post_pk>/',  post_detail, name='post_detail'),
    path('wall/<int:pk>/post/<int:post_pk>/edit/',  post_edit, name='post_edit'),
    path('wall/<int:pk>/post/<int:post_pk>/delete/',  post_delete, name='post_delete'),
    path('wall/post/<int:pk>/comment/<int:comment_pk>/edit/', comment_edit, name='comment_edit'),
    path('wall/post/<int:pk>/comment/<int:comment_pk>/delete/', comment_delete, name='comment_delete'),
]