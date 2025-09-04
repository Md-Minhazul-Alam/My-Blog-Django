from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('category/<slug:category_slug>', views.category_page, name='categoryPage'),
    path('blog-details/<slug:blog_slug>', views.blog_details, name='blogDetails'),
    path('page/<slug:page_slug>', views.website_page, name='page'),
    path('search-blogs/', views.search_list, name='searchList'), 
    # Comments Path
    path('blog/<slug:blog_slug>/add-comment/', views.add_comment, name='add_comment'),
    path('verify-comment-owner/', views.verify_comment_owner, name='verify_comment_owner'),
    path('edit-comment/', views.edit_comment, name='edit_comment'),
    path('delete-comment/', views.delete_comment, name='delete_comment'),
]
