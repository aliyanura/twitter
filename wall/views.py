from django.shortcuts import render, get_object_or_404
from .models import Wall, Post, Comment, Following
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.models import User


def Wall(request):
    posts = Post.objects.all()
    targets = Following.objects.all()
    return render(request, 'wall.html', locals())

def profile(request, pk):

    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.all()
    return render(request, 'profile.html', locals())