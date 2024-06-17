from django.db import models

# Modèle pour les articles
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title  # Représentation sous forme de chaîne du titre de l'article

    class Meta:
        indexes = [
            models.Index(fields=['title']),  # Index pour améliorer la recherche sur le titre
            models.Index(fields=['published_date']),  # Index pour améliorer la recherche par date de publication
        ]

# Modèle pour les structures
class Structure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['location']),
        ]

# Modèle pour les professionnels
class Professional(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=10)
    location = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        indexes = [
            models.Index(fields=['last_name']),
            models.Index(fields=['profession']),
            models.Index(fields=['location']),
        ]

# Modèle pour les événements
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['date']),
            models.Index(fields=['location']),
        ]
