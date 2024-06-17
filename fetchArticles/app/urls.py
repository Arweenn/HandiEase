from django.urls import path
from .views import index, getRSS, get_article_detail

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('articles/', getRSS, name='articles'),
    path('article/<int:article_id>/', get_article_detail, name='article_detail'),
]