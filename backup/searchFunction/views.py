from django.views.generic import TemplateView
from django.db.models import Q
from .models import Article, Structure, Professional, Event


# Vue pour les résultats de recherche
class SearchResultsView(TemplateView):


    def get_queryset(self):

        # Récupérer la requête de recherche et la catégorie depuis les paramètres GET
        query = self.request.GET.get('q', '')
        category = self.request.GET.get('category', '')

        results = []

        # Effectuer la recherche en fonction de la catégorie spécifiée
        if category == 'articles':
            results = list(Article.objects.filter(title__icontains=query))
        elif category == 'structures':
            results = list(Structure.objects.filter(name__icontains=query))
        elif category == 'professionals':
            results = list(Professional.objects.filter(
                Q(first_name__icontains=query) | 
                Q(last_name__icontains=query) | 
                Q(profession__icontains=query) | 
                Q(location__icontains=query)
            ))
        elif category == 'events':
            results = list(Event.objects.filter(
                Q(title__icontains=query) | 
                Q(date__icontains=query) | 
                Q(location__icontains=query)
            ))
        else:
            # Recherche dans toutes les catégories si aucune catégorie spécifique n'est donnée
            articles = list(Article.objects.filter(
                Q(title__icontains=query) | 
                Q(summary__icontains=query) | 
                Q(published__icontains=query)
            ))
            structures = list(Structure.objects.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query) | 
                Q(location__icontains=query)
            ))
            professionals = list(Professional.objects.filter(
                Q(first_name__icontains=query) | 
                Q(last_name__icontains=query) | 
                Q(profession__icontains=query) | 
                Q(location__icontains=query)
            ))
            events = list(Event.objects.filter(
                Q(title__icontains=query) | 
                Q(date__icontains=query) | 
                Q(location__icontains=query)
            ))
            results = articles + structures + professionals + events  # Combiner tous les résultats

        return results

    def get_context_data(self, **kwargs):

        # Obtenir le contexte de la vue parente
        context = super().get_context_data(**kwargs)

        # Ajouter les résultats de recherche au contexte
        context['object_list'] = self.get_queryset()

        # Ajouter la requête de recherche et la catégorie au contexte
        context['query'] = self.request.GET.get('q', '')
        context['category'] = self.request.GET.get('category', '')

        return context  # Retourner le contexte mis à jour
