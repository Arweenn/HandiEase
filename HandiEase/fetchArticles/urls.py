from django.urls import path
from .views import index, getRSS

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('articles/', getRSS, name='articles'),
]