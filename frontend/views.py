from django.views.decorators.cache import cache_page
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

@cache_page(864000)
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
    category_blogs = CategoryBlog.objects.select_related('category').all()

    for cb in category_blogs: 
        blogs = list(Blog.objects.filter(
            category=cb.category,
            is_active=True
        ).order_by('-id')[:10])

        if blogs:
            category_sections.append({
                'heading': cb.heading,
                'category': cb.category,
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

@cache_page(864000)
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
    # Most Viewed Blogs
    most_viewed = Blog.objects.filter(is_active=True).order_by('-views')[:5]

    # Get Comments
    comments = Comment.objects.filter(blog=details, is_active=True)
    # All Tags
    tags = details.tag.all()
    
    return render(request, "pages/blog-details.html", {
        'categories': categoryMenu,
        'socials': social, 
        'settings': setting,
        'pages': page,
        'editors': editor,
        'blogDetails': details,
        'comments': comments,
        'tags': tags, 
        'most_viewed': most_viewed,
    })

@cache_page(864000)
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
        try:
            data = json.loads(request.body.decode('utf-8'))
            comment_id = data.get('comment_id')
            email = data.get('email')
            
            if not comment_id or not email:
                return JsonResponse({
                    'success': False,
                    'message': 'Comment ID and email are required.'
                })
            
            comment = Comment.objects.get(id=comment_id, email=email, is_active=True)
            return JsonResponse({
                'success': True,
                'comment': {
                    'id': comment.id,
                    'name': comment.name,
                    'email': comment.email,
                    'comment': comment.comment
                }
            })
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data.'
            })
        except Comment.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Invalid email or comment not found.'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'An error occurred: {str(e)}'
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

# Edit Comment
@csrf_exempt
def edit_comment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            comment_id = data.get('comment_id')
            email = data.get('email')
            new_comment = data.get('comment')
            
            if not comment_id or not email or not new_comment:
                return JsonResponse({
                    'success': False,
                    'message': 'All fields are required.'
                })
            
            comment = Comment.objects.get(id=comment_id, email=email, is_active=True)
            comment.comment = new_comment
            comment.save()
            return JsonResponse({'success': True, 'message': 'Comment updated successfully!'})
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data.'
            })
        except Comment.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'You are not authorized to edit this comment.'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'An error occurred: {str(e)}'
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

# Delete Comment
@csrf_exempt
def delete_comment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            comment_id = data.get('comment_id')
            email = data.get('email')
            
            if not comment_id or not email:
                return JsonResponse({
                    'success': False,
                    'message': 'Comment ID and email are required.'
                })
            
            comment = Comment.objects.get(id=comment_id, email=email, is_active=True)
            comment.delete()
            return JsonResponse({'success': True, 'message': 'Comment deleted successfully!'})
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid JSON data.'
            })
        except Comment.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'You are not authorized to delete this comment.'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'An error occurred: {str(e)}'
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

