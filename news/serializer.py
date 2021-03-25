from rest_framework import serializers

from .models import Articles


class ListArticleSerializers(serializers.ModelSerializer):
    """Serializer List Articles"""
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Articles
        fields = ('user', 'title', 'create', 'moderation')


class DetailArticleSerializer(serializers.ModelSerializer):
    """Serializer Article"""
    class Meta:
        model = Articles
        fields = ('user', 'title', 'text', 'create', 'moderation', 'slug')


class CreateArticleSerializer(serializers.ModelSerializer):
    """Serializer Article"""
    class Meta:
        model = Articles
        fields = ('user', 'title', 'text', 'moderation')


class DeleteArticleSerializer(serializers.ModelSerializer):
    """Serializer Article"""
    class Meta:
        model = Articles


class UpdateArticleSerializer(serializers.ModelSerializer):
    """Serializer Article"""
    class Meta:
        model = Articles
        fields = ('title', 'text')
