from django.shortcuts import render, get_object_or_404, redirect
from .models import Wall, Post, Comment, Following
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.models import User
from .forms import FollowingForm


def home(request):
    posts = Post.objects.all()
    targets = Following.objects.all()
    return render(request, 'home.html', locals())

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', locals())

def wall_posts(request, pk):
    owner = get_object_or_404(User, pk=pk)
    return render(request, 'wall_posts.html', locals())

def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if post.like.owner is request.user:
            if post.like.is_pressed:
                post.likes_count -= 1
            else:
                post.likes_count += 1
        return redirect('post_detail', pk=pk)

        # if form.is_valid(): 
        #     topic = form.save(commit=False)
        #     topic.board = board
        #     topic.starter = request.user
        #     topic.save()
        #     post = Post.objects.create(
        #         message=form.cleaned_data.get('message'),
        #         topic=topic,    
        #         created_by=request.user
        #     )
        #     return redirect('topic_posts', pk=pk, topic_pk=topic.pk)


def follow(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        print('method - POST')
        form = FollowingForm(request.POST)
        if form.is_valid:
            following = form.save(commit=False)
            following.follower = request.user
            following.target = user
            following.save()
            return redirect('wall_posts', pk=pk)
    else:
        print("It's else")
        form = FollowingForm()
    return redirect('wall_posts', pk=pk)
