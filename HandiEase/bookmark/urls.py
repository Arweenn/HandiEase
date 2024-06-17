from django.urls import path
from .views import home, add_bookmark, BookmarkListView

urlpatterns = [
    path('', home, name='home'),
    path('add_bookmark/<int:content_type_id>/<int:object_id>/', add_bookmark, name='add_bookmark'),
    path('bookmarks/', BookmarkListView.as_view(), name='bookmark_list'),
]
