### Fonctions pour récupérer et afficher les articles RSS ###

from dateutil import parser as date_parser
from dateutil.tz import tzutc
import feedparser


# Vue pour récupérer et afficher les articles RSS
def getRSS():
    urls = [
        'https://www.handicap.fr/rss',
        'https://handirect.fr/feed',
        'https://actus.handicap.fr/rss',
        'https://www.carenews.com/taxonomy/term/27534/feed',
        'https://www.lemonde.fr/handicap/rss_full.xml',
        'https://www.francebleu.fr/rss/handicap.xml',
        'https://www.faire-face.fr/feed/',
        'https://www.unapei.org/flux-rss/',
        'https://www.cnsa.fr/restons-connectes',
    ]

    formatted_articles = []

    # Parcourir les flux RSS
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


# Fonction pour vérifier si un article est un podcast
def is_podcast(article):
    return any(link.get('type', '').startswith('audio') for link in article.get('links', []))


# Fonction pour filtrer l'image de l'article
def filter_image_from_article(article):

    filtered_article = article.copy()
    filtered_article.pop('image_url', None)

    return filtered_article


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


# Fonction pour filtrer les articles par requête de recherche
def filter_articles_by_query(articles, query):

    print(query)
    if not query:
        return articles

    filtered_articles = []

    for article in articles:
        if query.lower() in article['title'].lower() or query.lower() in article['summary'].lower():
            filtered_articles.append(article)
            print(article['title'] + "1")

    return filtered_articles


# Vue pour catégoriser les articles
def tags(article):

    tags = []

    if "handicap" in article['title'].lower() or "handicap" in article['summary'].lower():
        tags.append('handicap')
    if "inclusion" in article['title'].lower() or "inclusion" in article['summary'].lower():
        tags.append('inclusion')
    if "accessibilité" in article['title'].lower() or "accessibilité" in article['summary'].lower():
        tags.append('accessibilité')
    if "sport" in article['title'].lower() or "sport" in article['summary'].lower():
        tags.append('sport')

    return tags


# Vue pour filtrer les articles par tag
def filter_articles_by_tag(articles, tag_name):

    tagged_articles = []

    for article in articles:
        if tag_name.lower() in [tag.name.lower() for tag in article['tags']]:
            tagged_articles.append(article)

    return tagged_articles
