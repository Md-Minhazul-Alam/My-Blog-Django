from post.models import Category, Social, Blog, Page
from django.shortcuts import render
import requests 
from websitesetting.models import Setting
from django.shortcuts import get_object_or_404

# Create your views here.
def HomePage(request):
    # All Categories
    categoryMenu = Category.objects.all()
    #  Social
    social = Social.objects.all()
    # Website Setting
    setting = Setting.objects.latest('id')
    # Page
    page = Page.objects.all
    
    return render(request, "pages/home.html", {
        'categories': categoryMenu,
        'socials': social, 
        'settings': setting,
        'pages': page,
    })
    
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

    return render(request, "pages/category.html", {
        'categories': categoryMenu,
        'socials': social,
        'settings': setting,
        'blogs': blogs,
        'pages': page,
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
    page = get_object_or_404(Page, page_slug=page_slug, is_active=True)
    pageDetails = Page.objects.filter(page=page, is_active=True)
    
    return render(request, "pages/page.html", {
        'categories': categoryMenu,
        'socials': social, 
        'settings': setting,
        'pages': pageMenu,
        'pageInfo': pageDetails
    })