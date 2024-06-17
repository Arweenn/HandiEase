from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Formulaire d'inscription des utilisateurs
class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User  # Spécifie le modèle à utiliser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']  # Champs du formulaire

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})  # Ajout de classes CSS aux champs
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
