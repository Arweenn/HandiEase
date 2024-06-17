from django.shortcuts import render
from dateutil import parser as date_parser
from bs4 import BeautifulSoup, Tag
from dateutil.tz import tzutc
from .models import Article
import feedparser


# Vue pour afficher la page d'accueil
def index(request):
    return render(request, 'index.html')


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

    # Récupérer l'URL de l'image de l'article
    image_url = get_image_url(article)
    if image_url:
        formatted_article['image_url'] = image_url

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


# Fonction pour extraire l'URL de l'image de l'article
def get_image_url(article):
    if 'media_content' in article:
        return article.media_content[0].get('url')
    if 'media_thumbnail' in article:
        return article.media_thumbnail[0].get('url')
    
    soup = BeautifulSoup(article.summary, 'html.parser')
    img_tag = soup.find('img')
    if img_tag and isinstance(img_tag, Tag):
        return img_tag.get('src')
    return None


# Vue pour récupérer et afficher les articles RSS
def getRSS(request):
    urls = [
        'https://www.handicap.fr/rss',
        'https://handirect.fr/feed',
    ]

    for url in urls:
        feed = feedparser.parse(url)  # Parser le flux RSS
        articles = feed.entries

        for article in articles:
            if is_podcast(article):  # Ignorer les podcasts
                continue

            formatted_article = parse_article(article)  # Parser l'article

            # Mettre à jour ou créer l'article dans la base de données
            Article.objects.update_or_create(
                link=formatted_article['link'],
                defaults=formatted_article
            )

    # Récupérer tous les articles triés par date de publication
    formatted_articles = Article.objects.all().order_by('-published')
    context = {
        'articles': formatted_articles
    }
    return render(request, 'articles.html', context)
