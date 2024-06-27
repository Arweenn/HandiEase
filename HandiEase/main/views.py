from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import cache_page
from dateutil import parser as date_parser
from dateutil.tz import tzutc
from .models import Article, ReadingList
import feedparser
import logging

logger = logging.getLogger(__name__)

# Vue principale
def home(request):
    # add CSRF token to the context
    rss_articles = cache.get('cached_articles')  # Récupérer les articles en cache

    if not rss_articles:

        rss_articles = getRSS()
        cache.set('cached_articles', rss_articles)

    query = request.GET.get('q', '')  # Récupérer la requête de recherche depuis les paramètres GET
    articles = filter_articles_by_query(rss_articles, query)
    
    # Pagination
    paginator = Paginator(articles, 5)  # 5 articles par page
    page_num = request.GET.get('page')  # Récupérer le numéro de page demandé

    try:
        articles = paginator.page(page_num)  # Récupérer les articles de la page demandée
    except PageNotAnInteger:
        articles = paginator.page(1)  # Afficher la première page si le numéro de page n'est pas un entier
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)  # Afficher la dernière page si le numéro de page est trop grand

    context = {
        'articles': articles,
        'query': query,
        'user': request.user if request.user else None
    }

    # eviter la mise en cache de la page pour les utilisateurs connectés
    return render(request, 'homepage.html', context)



### Fonctions pour récupérer et afficher les articles RSS ###

# Fonction pour vérifier si un article est un podcast
def is_podcast(article):
    return any(link.get('type', '').startswith('audio') for link in article.get('links', []))


# Fonction pour parser un article et extraire les informations nécessaires
def parse_article(article):

    formatted_article = {
        'title': getattr(article, 'title', ''),
        'link': getattr(article, 'link', ''),
        'summary': getattr(article, 'summary', ''),
        'content': getattr(article, 'content', ''),
        'source': getattr(article, 'source', {}).get('title', ''),
        'published': parse_published_date(getattr(article, 'published', None))
    }

    return formatted_article


# Fonction pour parser la date de publication
def parse_published_date(published):

    if not published:
        return None
    
    try:
        published_date = date_parser.parse(published)
        
        if published_date.tzinfo is None:
            published_date = published_date.replace(tzinfo=tzutc())
            
        return published_date
    
    except (ValueError, TypeError):
        
        return None


# Fonction pour filtrer l'image de l'article
def filter_image_from_article(article):

    filtered_article = article.copy()
    filtered_article.pop('image_url', None)

    return filtered_article


# Vue pour récupérer et afficher les articles RSS
def getRSS():
    urls = [
        'https://www.handicap.fr/rss',
        'https://handirect.fr/feed',
        'https://actus.handicap.fr/rss',
        'https://www.carenews.com/taxonomy/term/27534/feed',
        'https://www.lemonde.fr/handicap/rss_full.xml',
    ]

    formatted_articles = []

    for url in urls:

        feed = feedparser.parse(url)
        articles = feed.entries

        for article in articles:

            if is_podcast(article):
                continue

            formatted_article = parse_article(article)
            filtered_article = filter_image_from_article(formatted_article)
            formatted_articles.append(filtered_article)

            default_date = date_parser.parse('1970-01-01T00:00:00Z').replace(tzinfo=tzutc())
            formatted_articles.sort(key=lambda x: x['published'] if x['published'] else default_date, reverse=True)

    return formatted_articles


# Fonction pour filtrer les articles par requête de recherche
def filter_articles_by_query(articles, query):

    if not query:
        return articles

    filtered_articles = []

    for article in articles:
        if query.lower() in article['title'].lower() or query.lower() in article['summary'].lower():
            filtered_articles.append(article)

    return filtered_articles


### Fonctions pour le login / register ###

# Vue pour l'inscription des utilisateurs
@csrf_exempt
def register_view(request):

    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('psw')
            email = request.POST.get('email')

            if User.objects.filter(username=username).exists():
                return JsonResponse({'success': False, 'message': 'Username already exists'})

            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()

            return JsonResponse({'success': True, 'message': 'Inscription réussie'})
        except Exception as e:
            logger.error(e)
            return JsonResponse({'success': False, 'message': 'Inscription échouée'}, status=400)
        
    return JsonResponse({'success': False, 'message': 'Inscription échouée'}, status=400)


# Vue pour la connexion des utilisateurs
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('psw')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                ## connect user for qll ti,es
                login(request, user)                
                
                return JsonResponse({'success': True, 'message': 'Connexion réussie'})
            else:
                return JsonResponse({'success': False, 'message': 'Nom d\'utilisateur ou mot de passe incorrect'}, status=400)
        except Exception as e:
            logger.error(e)
            return JsonResponse({'success': False, 'message': 'Nom d\'utilisateur ou mot de passe incorrect'})
    return JsonResponse({'success': False, 'message': 'Nom d\'utilisateur ou mot de passe incorrect'}, status=400)

@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({'success': True, 'message': 'Déconnexion réussie'})


### Vues pour la liste de lecture ###

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
