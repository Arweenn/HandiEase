from django.urls import path
from .views import getRSS

app_name = 'fetchArticles'

urlpatterns = [
    path('', getRSS, name='fetch_rss'),
]
