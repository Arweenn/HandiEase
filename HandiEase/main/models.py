from django.db import models
from django.contrib.auth.models import User

app_name = 'main'


# Modèle pour les articles
class Article(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()


    def __str__(self):
        return self.title  # Représentation sous forme de chaîne du titre de l'article


# Modèle pour la liste de lecture
class ReadingList(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article)


    def __str__(self):
        return f'{self.user.username} - {self.article.title}'
