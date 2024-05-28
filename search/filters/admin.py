from django.contrib import admin
from .models import Article, Structure, Professional, Event


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published_date')


class StructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location')


class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'profession', 'location')


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'location')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Structure, StructureAdmin)
admin.site.register(Professional, ProfessionalAdmin)
admin.site.register(Event, EventAdmin)
