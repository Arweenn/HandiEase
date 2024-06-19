from django.db import models

# Modèle pour les articles
class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    published = models.DateTimeField(null=True, blank=True)
    link = models.URLField(max_length=500)
    source = models.CharField(max_length=255)
    image_url = models.URLField(null=True, blank=True)
    content = models.JSONField()

    def __str__(self):
        return self.title  # Représentation sous forme de chaîne du titre de l'article

    class Meta:
        indexes = [
            models.Index(fields=['title']),  # Index pour améliorer la recherche sur le titre
            models.Index(fields=['published']),  # Index pour améliorer le tri et la recherche par date de publication
            models.Index(fields=['source']),  # Index pour améliorer la recherche par source
        ]
