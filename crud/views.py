from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm, TagForm
from django.core.paginator import Paginator


def top(request):
    latest_posts = BlogPost.objects.all().order_by('-date_published')[:4]
    return render(request, 'top.html', {'posts': latest_posts})

def contact_view(request):
    return render(request, 'contact.html')

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-date_published')
    return render(request, 'blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'post': post})

def blog_list(request):
    posts = BlogPost.objects.order_by('-date_published')
    paginator = Paginator(posts, 10)  # 1ページに10件の記事を表示
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html', {'page_obj': page_obj})