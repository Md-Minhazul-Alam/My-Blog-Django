from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('category/<slug:category_slug>', views.CategoryPage, name='categoryPage'),
    path('page/<slug:page_slug>', views.WebsitePage, name='page'),
]