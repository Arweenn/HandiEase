from django.urls import path
from django.contrib.auth import views as auth
from . import views


urls = [
    path('login/', views.login, name ='login'),
	path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
	path('register/', views.register, name ='register'),
    path('profil/', views.profile, name ='profil'),
    ]