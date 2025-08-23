from post.models import Category, Social, Blog, Page, CategoryBlog, Comment
from django.shortcuts import render
import requests 
from websitesetting.models import Setting
from django.shortcuts import get_object_or_404, redirect
from django.db.models import F, Q
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


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
        'category': category,
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
        'pageInfo': pageDetails,
    })

# Search Blogs
def searchList(request):
    # All Categories
    categoryMenu = Category.objects.all()
    #  Social
    social = Social.objects.all()
    # Website Setting
    setting = Setting.objects.latest('id')
    # Page
    pageMenu = Page.objects.all
    # Editor Choice
    editor = Blog.objects.filter(is_active=True, is_featured=True)[:6]
    # Most Viewed Blogs
    most_viewed = Blog.objects.filter(is_active=True).order_by('-views')[:5]
    # Search Blogs
    query = request.GET.get("keyword")
    blogs = Blog.objects.all()
    if query:
        blogs = blogs.filter(
            Q(blog_name__icontains=query) | Q(short_description__icontains=query) 
        )
    
    return render(request, "pages/search.html", {
        'categories': categoryMenu,
        'socials': social, 
        'settings': setting,
        'pages': pageMenu,
        'editors': editor,
        'most_viewed': most_viewed,
        'blogs': blogs,    
    })

# Add Comment
def add_comment(request, blog_slug):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, blog_slug=blog_slug)
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment_text = request.POST.get('comment')

        if name and email and comment_text:
            Comment.objects.create(
                blog=blog,
                name=name,
                email=email,
                comment=comment_text,
            )
            messages.success(request, 'Comments added successfully')
        else:
            messages.error(request, 'Please fill all the fields')
    return redirect('blogDetails', blog_slug=blog_slug)

# Verify Comment
@csrf_exempt
def verify_comment_owner(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comment_id = data.get('comment_id')
        email = data.get('email')

        try:
            comment = Comment.objects.get(id=comment_id, email=email, is_active=True),
            return JsonResponse({
               'success': True, 
               'comment': {
                   'id': comment.id, 
                   'name': comment.name,
                   'email': comment.email,
                   'comment': comment.comment
               } 
            })
        except Comment.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'invalid email or comment not found'
            })
    return JsonResponse({
        'success': False,
        'message': 'invalid request'
    })
# Edit Comment
def edit_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comment_id = data.get('comment_id')
        email = data.get('email')
        new_comment = data.get('comment')

        try:
            comment = Comment.objects.get(id=comment_id, email=email, is_active=True)
            comment.comment = new_comment
            comment.save()

            return JsonResponse({
                'success': True,
                'message': 'Comments updated successfully'
            })
        except Comment.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'You are not authorized to edit'
            })
    return JsonResponse({
        'success': False,
        'message': 'invalid request'
    })

# Delete Comment
def delete_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comment_id = data.get('comment_id')
        email = data.get('email')


        try:
            comment = Comment.objects.get(id=comment_id, email=email, is_active=True)
            comment.is_active = False
            comment.save()

            return JsonResponse({
                'success': True,
                'message': 'Comments deleted successfully'
            })
        except Comment.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'You are not authorized to edit'
            })
       
