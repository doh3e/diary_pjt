from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('diaries:index')
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('diaries:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
    

def login(request):
    if request.user.is_authenticated:
        return redirect('diaries:index')
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('diaries:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
    
@login_required
def logout(request):
    auth_logout(request)
    return redirect('diaries:index')

@login_required
def mypage(request, user_pk):
    pass