from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm


# Page d'accueil
def index(request):

    return render(request, 'index.html', {'title': 'index'})


# Vue pour l'inscription des utilisateurs
def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You are now able to log in.')

            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'index.html', {'form': form, 'title': 'register here'})


# Vue pour la connexion des utilisateurs
def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome {username}!')
                return redirect('logged_in')
            else:
                messages.error(request, 'Invalid username or password.')

        else:
            messages.error(request, 'Invalid username or password.')

    else:
        form = AuthenticationForm()

    return render(request, 'index.html', {'form': form, 'title': 'log in'})


# Vue pour le profil de l'utilisateur
@login_required
def profile(request):

    return render(request, 'profile.html', {'title': 'profile'})
