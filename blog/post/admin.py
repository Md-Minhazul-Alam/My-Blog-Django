from django.contrib import admin
from .models import Category, Tag, Blog, Social, Page
from websitesetting.models import Setting 

# Register Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_slug')
    search_fields = ('category_name', 'category_slug')

admin.site.register(Category, CategoryAdmin)

# Register Tag
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'tag_slug')
    search_fields = ('tag_name', 'tag_slug')

admin.site.register(Tag, TagAdmin)

# Register Blog
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_name', 'blog_slug')
    search_fields = ('blog_name', 'blog_slug')

admin.site.register(Blog, BlogAdmin)

# Register Social
class SocialAdmin(admin.ModelAdmin):
    list_display = ('social_name', 'social_link')
    search_fields = ('social_name', 'social_link')

admin.site.register(Social, SocialAdmin)

# Register Website Setting
class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_meta_keywords')
    search_fields = ('site_name', 'site_meta_keywords')

admin.site.register(Setting, WebsiteSettingAdmin)

# Register Page
class PageAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'page_slug')
    search_fields = ('page_name', 'page_slug')

admin.site.register(Page, PageAdmin)
