from post.models import Category, Social, Blog, Page, CategoryBlog
from django.shortcuts import render
import requests 
from websitesetting.models import Setting
from django.shortcuts import get_object_or_404
from django.db.models import F


# Home Page
def HomePage(request):
    categoryMenu = Category.objects.all()
    social = Social.objects.all()
    setting = Setting.objects.latest('id')
    page = Page.objects.all()
    editor = Blog.objects.filter(is_active=True, is_featured=True)[:6]

    # Slider
    sliders = Blog.objects.filter(is_active=True, is_featured=True)[:3]

    # Get Category Blog
    category_sections = []
    categories = Category.objects.filter(is_active=True)

    for category in categories:
        blogs = list(Blog.objects.filter(
            category=category,
            is_active=True
        ).order_by('-id')[:10])

        if blogs:
            category_sections.append({
                'category': category,
                'first_blog': blogs[0],
                'other_blog': blogs[1:], 
            })
    # Most Viewed Blogs
    most_viewed = Blog.objects.filter(is_active=True).order_by('-views')[:5]

    return render(request, "pages/home.html", {
        'categories': categoryMenu,
        'socials': social,
        'settings': setting,
        'pages': page,
        'editors': editor,
        'category_sections': category_sections, 
        'most_viewed': most_viewed,
        'sliders': sliders, 
    })

# Category Page    
def CategoryPage(request, category_slug):
    # All Categories
    categoryMenu = Category.objects.all()
    #  Social
    social = Social.objects.all()
    # Website Setting
    setting = Setting.objects.latest('id')
    # Category Blog
    category = get_object_or_404(Category, category_slug=category_slug, is_active=True)
    blogs = Blog.objects.filter(category=category, is_active=True)
    # Page
    page = Page.objects.all
     # Editor Choice
    editor = Blog.objects.filter(
        is_active=True,
        is_featured=True,
    )[:6]
    # Most Viewed Blogs
    most_viewed = Blog.objects.filter(is_active=True).order_by('-views')[:5]

    return render(request, "pages/category.html", {
        'categories': categoryMenu,
        'socials': social,
        'settings': setting,
        'blogs': blogs,
        'pages': page,
        'editors': editor,
        'most_viewed': most_viewed,
    })

# Blog Details
def blogDetails(request, blog_slug):
    # All Categories
    categoryMenu = Category.objects.all()
    #  Social
    social = Social.objects.all()
    # Website Setting
    setting = Setting.objects.latest('id')
    # Page
    page = Page.objects.all
    # Editor Choice
    editor = Blog.objects.filter(
        is_active=True,
        is_featured=True,
    )[:6]
    # Blog Details
    details = get_object_or_404(Blog, blog_slug = blog_slug)
    # View Count
    Blog.objects.filter(pk=details.pk).update(views=F('views') + 1)
    details.refresh_from_db()
    
    return render(request, "pages/blog-details.html", {
        'categories': categoryMenu,
        'socials': social, 
        'settings': setting,
        'pages': page,
        'editors': editor,
        'blogDetails': details,
    })

# Page
def WebsitePage(request, page_slug):
    # All Categories
    categoryMenu = Category.objects.all()
    #  Social
    social = Social.objects.all()
    # Website Setting
    setting = Setting.objects.latest('id')
    # Page
    pageMenu = Page.objects.all
    # Page
    pageDetails = get_object_or_404(Page, page_slug=page_slug)
    
    
    return render(request, "pages/page.html", {
        'categories': categoryMenu,
        'socials': social, 
        'settings': setting,
        'pages': pageMenu,
        'pageInfo': pageDetails
    })