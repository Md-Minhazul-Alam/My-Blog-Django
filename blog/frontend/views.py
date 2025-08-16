from post.models import Category, Social
from django.shortcuts import render
import requests 
from websitesetting.models import Setting

# Create your views here.
def HomePage(request):
    # All Categories
    category = Category.objects.all()
    #  Social
    social = Social.objects.all()
    # Website Setting
    setting = Setting.objects.latest('id')
    
    return render(request, "pages/home.html", {
        'categories': category,
        'socials': social, 
        'settings': setting,
    })
    
def CategoryPage(request, category_slug):
    # All Categories
    category = Category.objects.all()
    #  Social
    social = Social.objects.all()
    # Website Setting
    setting = Setting.objects.latest('id')

    return render(request, "pages/category.html", {
        'categories': category,
        'socials': social,
        'settings': setting,
    })