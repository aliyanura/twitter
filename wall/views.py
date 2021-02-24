from django.shortcuts import render
from .models import Wall, Post, Comment
from django.views.generic import ListView, DeleteView, CreateView, UpdateView


class WallListView(ListView):
    model = Wall
    template_name = 'base.html'
    context_object_name = 'posts'