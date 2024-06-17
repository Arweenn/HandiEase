"""HandiEase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import home
from fetchArticles.views import getRSS
from searchFunction.views import HomePageView, SearchResultsView
from userAuth.views import login, register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage', home, name='home'),
    path('articles/', getRSS, name='articles'),
    path('search/', HomePageView.as_view(), name='search'),
    path('search-results/', SearchResultsView.as_view(), name='search-results'),
    path('login-register/', login, name='login-register'),
    path('login-register/', register, name='login-register'),
]
