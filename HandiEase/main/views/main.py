### Vue principale ###

from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .fetchArticles import getRSS, filter_articles_by_query, filter_articles_by_tag
from ..models import Tag


def home(request):
    rss_articles = cache.get('cached_articles')  # Récupérer les articles en cache

    if not rss_articles:

        rss_articles = getRSS()
        cache.set('cached_articles', rss_articles)

    # Filtrage des articles, fonction de recherche
    query = request.GET.get('q', '')
    tag_name = request.GET.get('tag', '')

    articles = filter_articles_by_query(rss_articles, query)
    if tag_name:
        articles = filter_articles_by_tag(articles, tag_name)
    
    # Pagination
    paginator = Paginator(articles, 10)
    page_num = request.GET.get('page')

    try:
        articles = paginator.page(page_num)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {
        'articles': articles,
        'query': query,
        'tag_name': tag_name,
        'tags': Tag.objects.all(),
        'user': request.user if request.user else None
    }

    return render(request, 'homepage.html', context)
