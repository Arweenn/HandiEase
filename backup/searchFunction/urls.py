from django.urls import path
from .views import HomePageView, SearchResultsView


urlpatterns = [
    path('search-results/', SearchResultsView.as_view(), name='search_results'),
    path('search/', HomePageView.as_view(), name='search'),
]