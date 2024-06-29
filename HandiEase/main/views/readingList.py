### Vues pour la liste de lecture ###

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import Article, ReadingList


# Vue pour ajouter un article à la liste de lecture
@login_required
def add_to_reading_list(request, article_id):

    article = get_object_or_404(Article, pk=article_id)
    ReadingList.objects.get_or_create(user=request.user, article=article)
    messages.success(request, 'Article ajouté à votre liste.')

    return redirect('homepage')


# Vue pour retire un article de la liste de lecture
@login_required
def remove_from_reading_list(request, article_id):

    article = get_object_or_404(Article, pk=article_id)
    reading_list_item = ReadingList.objects.filter(user=request.user, article=article)
    if reading_list_item.exists():
        reading_list_item.delete()
        messages.success(request, 'Article retiré de votre liste.')

    else:
        messages.error(request, 'Article non trouvé.')

    return redirect('homepage')


# Vue pour afficher la liste de lecture de l'utilisateur
@login_required
def reading_list(request):

    reading_list = ReadingList.objects.filter(user=request.user).select_related('article')
    context = {
        'reading_list': reading_list,
    }

    return render(request, 'reading_list.html', context)
