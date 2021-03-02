from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import *
from django.contrib.auth.decorators import login_required
from wall.models import *

def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', locals())

def account_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.all()
    images = Image.objects.all()
    return render(request, 'account_detail.html', locals())

@login_required 
def account_edit(request):
    """
    Processes requests for the settings page, where users
    can edit their profiles.
    """
    if request.method == 'POST':
        form = AccountChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AccountChangeForm(instance=request.user)
    return render(request, 'account_edit.html', locals())
