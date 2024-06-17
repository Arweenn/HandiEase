from django.urls import path
from .views import getRSS

app_name = 'app'

urlpatterns = [
    path('articles/', getRSS, name='articles'),
]