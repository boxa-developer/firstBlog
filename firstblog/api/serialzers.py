from rest_framework import serializers
from .models import Author, Post, Tag


class AuthorSerializer(serializers.ModelSerializer):
    author_posts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = ['author_firstname', 'author_lastname', 'author_joined_date', 'author_posts']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_date', 'post_title', 'post_text', 'post_author', 'post_tags']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag_title']