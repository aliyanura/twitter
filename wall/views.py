from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.models import User
from .forms import *
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def Wall(request):
    posts_list = Post.objects.all()
    targets = Following.objects.all()

    search = request.GET.get('search', '')

    paginator = Paginator(posts_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'wall.html', {'posts' : posts, 'page':page, "targets": targets})

def search(request):
    search = request.GET.get('search', '')
    if search:
        users = User.objects.filter(username__icontains=search)
    else:
        users = User.objects.all()
    return render(request, 'search.html', locals())

def post_detail(request, pk, post_pk):
    post = get_object_or_404(Post, created_by__pk=pk, pk=post_pk)
    comments = post.comments.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            obj = Comment()
            obj.message = comment_form.cleaned_data['message']
            obj.created_by = request.user
            obj.post = post
            obj.save()

        try:
            like = Like.objects.get(post=post, owner=request.user)
            if like.owner == request.user:
                if like.is_pressed==True:
                    post.likes_count -= 1
                    like.is_pressed = False
                    post.save()
                    like.save()
                elif like.is_pressed==False:
                    print('bye')
                    post.likes_count += 1
                    like.is_pressed = True
                    post.save()
                    like.save()
        except:
            like = Like.objects.create(is_pressed=True, owner=request.user, post=post)
            post.likes_count  += 1
            post.save()

    else:
        comment_form = CommentForm()
    return render(request, 'post_detail.html', locals())

def comment_edit(request, pk, comment_pk):
    comment = get_object_or_404(Comment, post__pk=pk, pk=comment_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_at = timezone.now()
            comment.save()
            return redirect('post_detail', pk=comment.post.created_by.pk, post_pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_edit.html', locals())

def comment_delete(request, pk, comment_pk):
    comment = get_object_or_404(Comment, post__pk=pk, pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', pk=comment.post.created_by.pk, post_pk=comment.post.pk)
    return render(request, 'comment_delete.html', locals())

def post_add(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = user
            post.created_at = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.created_by.pk, post_pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_add.html', locals())

def post_edit(request, pk, post_pk):
    post = get_object_or_404(Post, created_by__pk=pk, pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.created_by.pk, post_pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', locals())

def post_delete(request, pk, post_pk):
    post = get_object_or_404(Post, created_by__pk=pk, pk=post_pk)
    if request.method == 'POST':
        post.delete()
        return redirect('account_detail', pk=post.created_by.pk)
    return render(request, 'post_delete.html', locals())

def add_foto(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = user
            obj.save()
            return redirect('account_detail', pk)
    else:
        form = ImageForm()
    return render(request, 'add_foto.html', locals())

def change_foto(request, pk, image_pk):
    image = get_object_or_404(Image, owner_id=pk, pk=image_pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('account_detail', request.user.pk)
    else:
        form = ImageForm(instance=image)
    return render(request, 'change_foto.html', locals())


def follow(request, pk):
    user = get_object_or_404(User, pk=pk)
    follow = Following.objects.get(target=user, follower=request.user)
    if follow:
        follow.delete()
    else:
        follow = Following.objects.create(target=user, follower=request.user)
    return redirect('account_detail', pk=pk)