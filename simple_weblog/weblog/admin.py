from django.contrib import admin
from django.contrib.admin import register
from .models import Article, Comment


# Register your models here.
@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'topic')


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author')
    list_display_links = ('id', 'text')
    list_filter = ('author',)
