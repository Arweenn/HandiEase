from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    published = models.DateTimeField(null=True, blank=True)
    link = models.URLField(max_length=500)
    source = models.CharField(max_length=255)
    image_url = models.URLField(null=True, blank=True)
    content = models.JSONField()

    def __str__(self):
        return self.title
