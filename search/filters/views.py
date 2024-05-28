from django.views.generic import TemplateView
from django.db.models import Q
from .models import Article, Structure, Professional, Event

class HomePageView(TemplateView):
    template_name = "search.html"

class SearchResultsView(TemplateView):
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        category = self.request.GET.get('category', '')

        results = []

        if category == 'articles':
            results = list(Article.objects.filter(title__icontains=query))
        elif category == 'structures':
            results = list(Structure.objects.filter(name__icontains=query))
        elif category == 'professionals':
            results = list(Professional.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(profession__icontains=query) | Q(location__icontains=query)))
        elif category == 'events':
            results = list(Event.objects.filter(Q(name__icontains=query) | Q(date__icontains=query) | Q(location__icontains=query)))
        else:
            articles = list(Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(published_date__icontains=query)))
            structures = list(Structure.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(location__icontains=query)))
            professionals = list(Professional.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(profession__icontains=query) | Q(location__icontains=query)))
            events = list(Event.objects.filter(Q(name__icontains=query) | Q(date__icontains=query) | Q(location__icontains=query)))
            results = articles + structures + professionals + events

        print(results)
        return results


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.get_queryset()
        context['query'] = self.request.GET.get('q', '')
        context['category'] = self.request.GET.get('category', '')
        return context
