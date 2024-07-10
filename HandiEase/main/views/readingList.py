### Vues pour la liste de lecture ###

import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ..models import Article, ReadingList

logger = logging.getLogger(__name__)


@login_required
def add_to_reading_list(request):
    if request.method == 'POST':
        article_title = request.POST.get('article_title')
        
        try:
            article = Article.objects.get(title=article_title)
        except Article.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': "L'article n'existe pas."})

        reading_list, created = ReadingList.objects.get_or_create(user=request.user)
        
        # Vérifier si l'article est déjà dans la liste de lecture
        if article not in reading_list.articles.all():
            reading_list.articles.add(article)
            message = "L'article a été ajouté à votre liste de lecture."
        else:
            message = "L'article est déjà dans votre liste de lecture."

        return JsonResponse({'status': 'success', 'message': message})
    return JsonResponse({'status': 'error', 'message': 'Requête invalide.'})


@login_required
def remove_from_reading_list(request):
    if request.method == 'POST':
        article_title = request.POST.get('article_title')
        
        try:
            article = Article.objects.get(title=article_title)
        except Article.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': "L'article n'existe pas."})

        try:
            reading_list = ReadingList.objects.get(user=request.user)
        except ReadingList.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Liste de lecture introuvable.'})

        if article in reading_list.articles.all():
            reading_list.articles.remove(article)
            return JsonResponse({'status': 'success', 'message': "L'article a été retiré de votre liste de lecture."})
        else:
            return JsonResponse({'status': 'error', 'message': "L'article n'est pas dans votre liste de lecture."})
    return JsonResponse({'status': 'error', 'message': 'Requête invalide.'})


@login_required
def reading_list(request):
    try:
        reading_list = ReadingList.objects.get(user=request.user)
        articles = reading_list.articles.all()
        context = {
            'reading_list': articles,
        }
        return render(request, 'reading_list.html', context)

    except ReadingList.DoesNotExist:
        # Si la liste de lecture n'existe pas encore pour cet utilisateur, retourner une liste vide
        context = {
            'reading_list': [],
        }
        return render(request, 'reading_list.html', context)

