from django.shortcuts import render
from .models import Wall, Post, Comment, Following
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.models import User


def Wall(request):
    posts = Post.objects.all()
    targets = Following.objects.all()
    return render(request, 'wall.html', locals())

