from django.contrib import admin
from .models import Category, Tag, Blog, Social
from websitesetting.models import Setting

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

class SocialAdmin(admin.ModelAdmin):
    list_display = ('social_name', 'social_link')
    search_fields = ('social_name', 'social_link')

admin.site.register(Social, SocialAdmin)

class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_meta_keywords')
    search_fields = ('site_name', 'site_meta_keywords')

admin.site.register(Setting, WebsiteSettingAdmin)
