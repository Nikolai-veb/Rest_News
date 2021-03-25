from django.contrib import admin

from .models import Articles


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'moderation', 'create')
    list_display_links = ('id', 'title')
    list_filter = ('create', 'user')
    list_editable = ('moderation',)
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
