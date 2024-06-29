### Fonctions pour le login / register ###

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Vue pour l'inscription des utilisateurs
@csrf_exempt
def register_view(request):

    if request.method == 'POST':

        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')

            if User.objects.filter(username=username).exists():
                return JsonResponse({'success': False, 'message': 'Username already exists'})

            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()

            return JsonResponse({'success': True, 'message': 'Inscription réussie'})

        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Erreur lors de l\'inscription'}, status=400)
        
    return JsonResponse({'success': False, 'message': 'Inscription échouée'}, status=400)


# Vue pour la connexion des utilisateurs
@csrf_exempt
def login_view(request):

    if request.method == 'POST':

        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)                
                
                return JsonResponse({'success': True, 'message': 'Connexion réussie'})
            else:
                return JsonResponse({'success': False, 'message': 'Nom d\'utilisateur ou mot de passe incorrect'}, status=400)

        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Erreur lors de la connexion'}, status=400)

    return JsonResponse({'success': False, 'message': 'Nom d\'utilisateur ou mot de passe incorrect'}, status=400)


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({'success': True, 'message': 'Déconnexion réussie'})
