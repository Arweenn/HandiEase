from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Bookmark


# # Décorateur pour s'assurer que seul un utilisateur connecté peut accéder à cette vue.
# @login_required
# def home(request):

#     # Renvoie la page d'accueil.
#     return render(request, 'home.html')


@login_required
def add_bookmark(request, content_type_id, object_id):

    # Récupérer le ContentType à partir de l'ID, sinon renvoie un 404.
    content_type = get_object_or_404(ContentType, id=content_type_id)
    
    # Créer un objet Bookmark pour l'utilisateur connecté.
    Bookmark.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=object_id
    )

    # Rediriger l'utilisateur vers la liste des favoris.
    return redirect('bookmarks')


# Vue basée sur une classe pour afficher la liste des favoris de l'utilisateur connecté, utilisant ListView.
class BookmarkListView(ListView):

    model = Bookmark
    template_name = 'bookmarks.html'
    context_object_name = 'bookmarks'

    # Récupérer les favoris de l'utilisateur connecté.
    def get_queryset(self):

        # Utiliser select_related pour éviter les requêtes supplémentaires.
        return Bookmark.objects.filter(user=self.request.user).select_related('content_type')
