from post.models import Category
from django.shortcuts import render
import requests

# Create your views here.
def HomePage(request):
    category = Category.objects.all()
    
    return render(request, "pages/home.html", {
        'categories': category, 
    })

def CategoryPage(request, category_slug):
    category = Category.objects.all()

    return render(request, "pages/category.html", {
        'categories': category,
    })