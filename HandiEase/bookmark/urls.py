from django.urls import path
from .views import add_bookmark, BookmarkListView

urlpatterns = [
    path('add_bookmark/<int:content_type_id>/<int:object_id>/', add_bookmark, name='add_bookmark'),
    path('bookmarks/', BookmarkListView.as_view(), name='bookmarks'),
]
