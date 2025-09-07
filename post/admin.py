from django.contrib import admin
from .models import Category, Tag, Blog, Social, Page, CategoryBlog, Comment
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

class BlogTagInline(admin.TabularInline): 
    model = Blog.tag.through   
    extra = 1
    autocomplete_fields = ['tag']

# Register Blog
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_name', 'blog_slug', 'category', 'is_active', 'is_featured')
    search_fields = ('blog_name', 'blog_slug')
    list_filter = ('category', 'is_active', 'is_featured')
    filter_horizontal = ('tag',)

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

# Category Blog
class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ('heading', 'category')
    search_fields = ('heading', 'category')
    
admin.site.register(CategoryBlog, CategoryBlogAdmin)

# Comments Register
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'blog', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'comment')
    ordering = ('-created_at',)
