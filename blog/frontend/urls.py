from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('category/<slug:category_slug>', views.CategoryPage, name='categoryPage'),
    path('blog-details/<slug:blog_slug>', views.blogDetails, name='blogDetails'),
    path('page/<slug:page_slug>', views.WebsitePage, name='page'),
    path('search-blogs/', views.searchList, name='searchList'), 
    # Comments Path
    path('blog/<slug:blog_slug>/add-comment/', views.add_comment, name='add_comment'),
    path('verify-comment-owner/', views.verify_comment_owner, name='verify_comment_owner'),
    path('edit-comment/', views.edit_comment, name='edit_comment'),
    path('delete-comment/', views.delete_comment, name='delete_comment'),
    
]