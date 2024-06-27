from django.contrib import admin
from django.urls import path
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('register/', views.register_view, name="register_view"),
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),
    path('reading_list', views.reading_list, name="reading_list"),
    path('add_to_reading_list/<int:article_id>/', views.add_to_reading_list, name="add_to_reading_list"),
    path('remove_from_reading_list/<int:article_id>/', views.remove_from_reading_list, name="remove_from_reading_list"),
]
