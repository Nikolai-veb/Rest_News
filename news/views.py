from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions
from .models import Articles
from . import serializer


class ListArticleView(ListAPIView):
    """List Articles View"""
    serializer_class = serializer.ListArticleSerializers
    queryset = Articles.objects.filter(moderation=True).only('user', 'title', 'create', 'moderation')


class DetailArticleView(RetrieveAPIView):
    """Detail Article View"""
    serializer_class = serializer.DetailArticleSerializer
    queryset = Articles.objects.filter(moderation=True).defer('update',)
    lookup_field = 'slug'


class CreateArticleView(CreateAPIView):
    """Add Article View"""
    serializer_class = serializer.CreateArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'


class UpdateArticleView(UpdateAPIView):
    """Update Article View"""
    serializer_class = serializer.UpdateArticleSerializer
    queryset = Articles.objects.filter(moderation=True).only('title', 'text')
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'


class DeleteArticleView(DestroyAPIView):
    """Delete Article View"""
    serializer_class = serializer.DeleteArticleSerializer
    queryset = Articles.objects.filter(modertion=True)
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'
