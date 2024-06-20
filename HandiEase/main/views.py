from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from dateutil import parser as date_parser
from dateutil.tz import tzutc
import feedparser


# Vue principale
@cache_page(60 * 30)  # Cache la vue pendant 30 minutes
def home(request):

    rss_articles = cache.get('cached_articles')  # Récupérer les articles en cache
    if not rss_articles:
        rss_articles = getRSS()
        cache.set('cached_articles', rss_articles)

    query = request.GET.get('q', '')  # Récupérer la requête de recherche depuis les paramètres GET

    if query:  # Si une requête de recherche est spécifiée
        articles = [article for article in rss_articles if query.lower() in article['title'].lower()]
    else:
        articles = rss_articles
    
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
    }

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
        'https://handicap.paris.fr/feed/',
        'https://actus.handicap.fr/rss',
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
