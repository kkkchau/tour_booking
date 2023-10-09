from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms.user_forms import UserRegistrationForm, UserLoginForm
from .forms.tour_form import TourForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'tours/register_user.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'tours/login_user.html', {'form': form})

def add_tour(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = TourForm()

    return render(request, 'tours/add_tour.html', {'form': form})

def home(request):
    return render(request, 'tours/home.html')
