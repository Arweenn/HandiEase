from django.shortcuts import render


# Vue pour la page d'accueil
def home(request):
    return render(request, 'homepage.html')
