from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Professional(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    location = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Structure(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100, default='')
    description = models.TextField()

    def __str__(self):
        return self.name


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ['user', 'content_type', 'object_id']