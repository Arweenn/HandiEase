### Vues pour la liste de lecture ###

import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

logger = logging.getLogger(__name__)


@login_required
@require_POST
def add_to_reading_list(request):
    article_title = request.POST.get('article_title')
    if not article_title:
        return JsonResponse({'status': 'error', 'message': 'Titre de l\'article non fourni.'})

    reading_list = request.session.get('reading_list', [])
    if article_title not in reading_list:
        reading_list.append(article_title)
        request.session['reading_list'] = reading_list
        print(f"Article ajouté: {article_title}")
        print(f"Liste de lecture actuelle: {request.session['reading_list']}")

        return JsonResponse({'status': 'success', 'message': 'Article ajouté à votre liste de lecture.'})
    else:
        return JsonResponse({'status': 'info', 'message': 'Cet article est déjà dans votre liste de lecture.'})

@login_required
@require_POST
def remove_from_reading_list(request):
    article_title = request.POST.get('article_title')
    print("Article title received for removal: ", article_title)
    
    if not article_title:
        return JsonResponse({'status': 'error', 'message': 'Titre de l\'article non fourni.'})

    reading_list = request.session.get('reading_list', [])
    if article_title in reading_list:
        reading_list.remove(article_title)
        request.session['reading_list'] = reading_list

        # Ajout du message de debug
        print(f"Article retiré: {article_title}")
        print(f"Liste de lecture actuelle: {request.session['reading_list']}")

        return JsonResponse({'status': 'success', 'message': 'Article retiré de votre liste de lecture.'})
    else:
        return JsonResponse({'status': 'info', 'message': 'Cet article n\'est pas dans votre liste de lecture.'})



@login_required
def reading_list(request):
    reading_list = request.session.get('reading_list', [])
    context = {
        'reading_list': reading_list,
    }
    return render(request, 'reading_list.html', context)

