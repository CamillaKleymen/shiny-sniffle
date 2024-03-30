from django.contrib import admin
from .models import CategoryModel, News

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'created_at']
    search_fields = ['category_title']
    list_filter = ['created_at']
    ordering = ['category_title']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'description', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    ordering = ['title']
