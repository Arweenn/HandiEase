from django.shortcuts import render


# Vue pour la page d'accueil
def home(request):

    context = {
        'title': 'HandiEase',
        'content': 'Bienvenue sur HandiEase.'
    }
    return render(request, 'homepage.html', context)
