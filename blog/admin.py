from django.contrib import admin

from .models import Post


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')  # боковой толбар с фильтрами
    search_fields = ('title', 'body')  # текстовое поле для поиска по указанным атрибутам
    prepopulated_fields = {'slug': ('title',)}  # с вводом title, поле slug заполняется автоматом
    raw_id_fields = ('author',)
    date_hierarchy = "publish"  # появляется пагинация по датам
    ordering = ('status', 'publish')

