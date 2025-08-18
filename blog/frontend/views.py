from post.models import Category, Social, Blog, Page
from django.shortcuts import render
import requests 
from websitesetting.models import Setting
from django.shortcuts import get_object_or_404

# Home Page
def HomePage(request):
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
    
    return render(request, "pages/home.html", {
        'categories': categoryMenu,
        'socials': social, 
        'settings': setting,
        'pages': page,
        'editors': editor,
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

    return render(request, "pages/category.html", {
        'categories': categoryMenu,
        'socials': social,
        'settings': setting,
        'blogs': blogs,
        'pages': page,
        'editors': editor,
    })

# Blog Details
def blogDetails(request):
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
    
    return render(request, "pages/home.html", {
        'categories': categoryMenu,
        'socials': social, 
        'settings': setting,
        'pages': page,
        'editors': editor,
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