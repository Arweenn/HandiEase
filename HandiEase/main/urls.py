from django.urls import path, include
from .views import home


urlpatterns = [
    path('homepage/', home, name='homepage'),
    path('articles/', include('articles.urls')),
    path('search/', include('search.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('login-regiester/', include('userAuth.urls')),
]
