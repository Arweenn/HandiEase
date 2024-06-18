from django.contrib import admin
from django.urls import path
from main import views
from fetchArticles.views import getRSS
from userAuth.views import login, register, profile
from django.contrib.auth import views as auth_views
from searchFunction.views import HomePageView, SearchResultsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('articles/', getRSS, name='articles'),
    path('search/', HomePageView.as_view(), name='search'),
    path('search-results/', SearchResultsView.as_view(), name='search_results'),
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('register/', register, name='register'),
    path('profil/', profile, name='profil'),
]
