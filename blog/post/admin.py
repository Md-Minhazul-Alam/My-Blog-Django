from django.contrib import admin
from .models import Category, Tag, Blog

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_slug')
    search_fields = ('category_name', 'category_slug')

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'tag_slug')
    search_fields = ('tag_name', 'tag_slug')

admin.site.register(Tag, TagAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_name', 'blog_slug')
    search_fields = ('blog_name', 'blog_slug')

admin.site.register(Blog, BlogAdmin)
