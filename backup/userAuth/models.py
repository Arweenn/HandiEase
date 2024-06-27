from django.db import models


class User(models.Model):

    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)


    def __str__(self):

        return self.username  # Représentation sous forme de chaîne de l'utilisateur


    class Meta:

        verbose_name = 'User'  # Nom de l'entité dans l'interface d'administration
        verbose_name_plural = 'Users'  # Nom de l'entité au pluriel dans l'interface d'administration
