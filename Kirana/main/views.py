from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'main/home.html', {})

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'main/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'main/login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'main/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('home')