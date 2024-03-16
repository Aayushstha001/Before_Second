from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

def home(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {'category': category, 'product': product}
    return render(request, 'main/home.html', context)

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('register_info')
    else:
        form = UserForm()
    return render(request, 'pages/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'pages/login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'pages/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def register_info(request):
    form = InfoForm()

    if request.method == "POST":
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                info = form.save(commit=False)
                info.user = request.user
                info.save()
                messages.success(request, 'Info registered successfully.')
                return redirect('home')
            except Exception as e:
                messages.error(request, f'Error occurred during registration: {e}')
        else:
            messages.error(request, 'Error occurred during registration.')

    context = {'form': form}
    return render(request, 'pages/info_register.html', context)