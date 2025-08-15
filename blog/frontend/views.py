from django.shortcuts import render
import requests

# Create your views here.
def HomePage(request):

    return render(request, "pages/home.html")