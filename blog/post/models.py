from django.db import models
from django.utils.text import slugify

# Category
class Category(models.Model):
    category_name = models.CharField(max_length=200, default='')
    category_slug = models.SlugField(max_length=200, unique=True, blank=True, default='')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        # If slug is empty, generate from tag
        if not self.category_slug:
            base_slug = slugify(self.category_name)
        else:
            base_slug = slugify(self.category_slug)

        # Ensure uniqueness
        slug = base_slug
        num = 1
        while Category.objects.filter(category_slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{num}"
            num += 1

        self.category_slug = slug
        super().save(*args, **kwargs)
  
 # Tag   
class Tag(models.Model):
    tag_name = models.CharField(max_length=200, default='')
    tag_slug = models.SlugField(max_length=200, unique=True, blank=True, default='')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.tag_name
    
    def save(self, *args, **kwargs):
        # If slug is empty, generate from tag
        if not self.tag_slug:
            base_slug = slugify(self.tag_name)
        else:
            base_slug = slugify(self.tag_slug)

        # Ensure uniqueness
        slug = base_slug
        num = 1
        while Tag.objects.filter(tag_slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{num}"
            num += 1

        self.tag_slug = slug
        super().save(*args, **kwargs)

# Blog  
class Blog(models.Model):
    blog_name = models.CharField(max_length=200, default='')
    blog_slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True, related_name='blogs')
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='post', null=True, blank=True)
    keywords = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.blog_name

    def save(self, *args, **kwargs):
        # If slug is empty, generate from tag
        if not self.blog_slug:
            base_slug = slugify(self.blog_name)
        else:
            base_slug = slugify(self.blog_slug)

        # Ensure uniqueness
        slug = base_slug
        num = 1
        while Blog.objects.filter(blog_slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{num}"
            num += 1

        self.blog_slug = slug
        super().save(*args, **kwargs)

 # Social   
class Social(models.Model):
    social_name = models.CharField(max_length=200, default='')
    social_icon = models.TextField(default='')
    social_link = models.TextField(default='')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.social_name
    
# Page  
class Page(models.Model):
    page_name = models.CharField(max_length=200, default='')
    page_slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, default='')
    description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.page_name

    def save(self, *args, **kwargs):
        # If slug is empty, generate from tag
        if not self.page_slug:
            base_slug = slugify(self.page_name)
        else:
            base_slug = slugify(self.page_slug)

        # Ensure uniqueness
        slug = base_slug
        num = 1
        while Page.objects.filter(page_slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{num}"
            num += 1

        self.page_slug = slug
        super().save(*args, **kwargs)
