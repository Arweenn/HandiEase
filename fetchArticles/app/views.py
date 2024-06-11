from django.shortcuts import render
from bs4 import BeautifulSoup
import feedparser
from dateutil import parser as date_parser
from dateutil.tz import tzutc


def is_podcast(article):
    return any(link.get('type').startswith('audio') for link in article.links)


def getRSS(request):

    urls = [
        'https://www.handicap.fr/rss',
        'https://handirect.fr/feed',
        'https://www.lemonde.fr/handicap/rss_full.xml'
    ]

    formatted_articles = []
    for url in urls:
        feed = feedparser.parse(url)
        articles = feed.entries

        for article in articles:

            if is_podcast(article):
                continue

            formatted_article = {
                'title': article.title,
                'link': article.link,
                'summary': article.summary,
                'source': article.source.title if hasattr(article, 'source') else '',
            }

            if hasattr(article, 'published'):
                try:
                    published_date = date_parser.parse(article.published)
                    if published_date.tzinfo is None:
                        published_date = published_date.replace(tzinfo=tzutc())
                    formatted_article['published'] = published_date
                except (ValueError, TypeError):
                    formatted_article['published'] = None
            else:
                formatted_article['published'] = None

            image_url = None
            if 'media_content' in article:
                image_url = article.media_content[0]['url']
            elif 'media_thumbnail' in article:
                image_url = article.media_thumbnail[0]['url']
            else:
                soup = BeautifulSoup(article.summary, 'html.parser')
                img_tag = soup.find('img')
                if img_tag and isinstance(img_tag, BeautifulSoup):
                    image_url = img_tag.get('src')

            if image_url:
                formatted_article['image_url'] = image_url

            formatted_articles.append(formatted_article)

    default_date = date_parser.parse('1970-01-01T00:00:00Z').replace(tzinfo=tzutc())
    formatted_articles = sorted(
        formatted_articles,
        key=lambda x: x['published'] if x['published'] else default_date,
        reverse=True
    )    

    context = {
        'articles': formatted_articles
    }

    return render(request, 'index.html', context)
