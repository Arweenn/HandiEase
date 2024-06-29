from django.urls import path
from .views import main, authentication


urlpatterns = [
    path('', main.home, name='homepage'),
    path('register/', authentication.register_view, name='register_view'),
    path('login/', authentication.login_view, name='login_view'),
    path('logout/', authentication.logout_view, name='logout_view'),
]
