from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Bookmark

def home(request):
    return render(request, 'home.html')


def add_bookmark(request, content_type_id, object_id):
    content_type = get_object_or_404(ContentType, model=content_type_id)
    Bookmark.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=object_id
    )
    return redirect('bookmark_list')


def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmark_list.html', {'bookmarks': bookmarks})

