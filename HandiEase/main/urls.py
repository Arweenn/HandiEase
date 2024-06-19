from django.urls import path
from .views import home, getRSS


urlpatterns = [
    path('', home, name='homepage'),
    path('/', getRSS, name='getRSS'),
]
