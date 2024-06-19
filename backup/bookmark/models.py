from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Modèle pour les articles
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title  # Représentation sous forme de chaîne du titre de l'article

    class Meta:
        indexes = [
            models.Index(fields=['title']),  # Index pour améliorer la recherche
        ]

# Modèle pour les événements
class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['date']),
        ]

# Modèle pour les professionnels
class Professional(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    location = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        indexes = [
            models.Index(fields=['last_name']),
            models.Index(fields=['profession']),
        ]

# Modèle pour les structures
class Structure(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100, default='')
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

# Modèle pour les signets (bookmarks)
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisateur qui a créé le signet
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Type de contenu (générique)
    object_id = models.PositiveIntegerField()  # ID de l'objet associé au type de contenu
    content_object = GenericForeignKey('content_type', 'object_id')  # Référence générique à l'objet

    class Meta:
        unique_together = ['user', 'content_type', 'object_id']  # Contrainte d'unicité pour éviter les doublons de signets
        indexes = [
            models.Index(fields=['user', 'content_type', 'object_id']),  # Index pour améliorer les performances de requête
        ]
