from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Author, Tag, Post


@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('author_lastname', 'author_firstname')
    list_display = ['author_lastname', 'author_firstname', 'author_joined_date']

    class Meta:
        model = Author


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ['tag_title']

    class Meta:
        model = Tag


@register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ['post_date']
    list_display = ['post_title', 'post_author', 'post_date']

    class Meta:
        model = Post
