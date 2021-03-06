from django.shortcuts import render, get_object_or_404
from blog.models import Blog, Tag, Category, Comment

# Create your views here.


def all_blogs(request):
    return render(request, 'blog/blog.html', context={
        'posts': Blog.objects.order_by('created_at')[:20],
        'selected_posts': Blog.objects.order_by('created_at')[:3],
        'tags': Tag.objects.all(),
        'categories': Category.objects.all(),
        'title': 'Allaia Blog &amp; News',
    })


def blog_view(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(blog=post)
    return render(request, 'blog/blog-post.html', context={
        'post': post,
        'comments': comments,
        'selected_posts': Blog.objects.order_by('created_at')[:3],
        'tags': Tag.objects.all(),
        'categories': Category.objects.all(),
    })


def category(request, slug):
    return render(request, 'blog/blog.html', context={
        'posts': Blog.objects.filter(category__slug=slug).order_by('created_at')[:20],
        'selected_posts': Blog.objects.order_by('created_at')[:3],
        'tags': Tag.objects.all(),
        'categories': Category.objects.all(),
        'title': 'Allaia Blog &amp; News | ' + Category.objects.get(slug=slug).name,
    })
