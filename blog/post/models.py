from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200, default='')
    category_slug = models.SlugField(max_length=200, unique=True, default='')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.category_name
    
class Tag(models.Model):
    tag_name = models.CharField(max_length=200, default='')
    tag_slug = models.SlugField(max_length=200, unique=True, default='')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.tag_name
    
class Blog(models.Model):
    blog_name = models.CharField(max_length=200, default='')
    blog_slug = models.SlugField(max_length=200, unique=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True, related_name='blogs')
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='post', null=True, blank=True)
    keywords = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.blog_name
