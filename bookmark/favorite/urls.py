from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_bookmark/<str:model_name>/<int:object_id>/', views.add_bookmark, name='add_bookmark'),
    path('bookmarks/', views.bookmark_list, name='bookmark_list'),
]
