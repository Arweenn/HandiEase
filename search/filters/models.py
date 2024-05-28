from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title


class Structure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Professional(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
