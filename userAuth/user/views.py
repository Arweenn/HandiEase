from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm


# index page
def index(request):
	return render(request, 'index.html', {'title':'index'})

# register forms 
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'index.html', {'form': form, 'title':'register here'})

# login forms
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		messages.success(request, f' welcome {username} !!')
		return redirect('index')

	form = AuthenticationForm()
	return render(request, 'index.html', {'form':form, 'title':'log in'})

