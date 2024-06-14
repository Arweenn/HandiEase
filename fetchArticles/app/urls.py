from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.getRSS, name='articles'),
    path('events/', views.getEvent, name='events'),
]