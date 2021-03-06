import math

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from blog.models import Blog, Tag, Category, Comment

# Create your views here.


def all_blogs(request):

    page = int(request.GET.get('page', 0))
    posts = Blog.objects.order_by('created_at')

    return render(request, 'blog/blog.html', context={
        'posts': posts[page*20:(page+1)*20],
        'selected_posts': Blog.objects.filter(selected=True).order_by('created_at')[:4],
        'tags': Tag.objects.all(),
        'categories': Category.objects.all(),
        'title': 'Allaia Blog &amp; News',
        'current_page': page,
        'pages_count': math.ceil(len(posts) / 20.),
    })


def blog_view(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(blog=post)
    return render(request, 'blog/blog-post.html', context={
        'post': post,
        'comments': comments,
        'selected_posts': Blog.objects.filter(selected=True).order_by('created_at')[:4],
        'tags': Tag.objects.all(),
        'categories': Category.objects.all(),
    })


def category(request, slug):

    page = int(request.GET.get('page', 0))
    posts = Blog.objects.filter(category__slug=slug).order_by('created_at')

    return render(request, 'blog/category.html', context={
        'posts': posts[page*20:(page+1)*20],
        'selected_posts': Blog.objects.filter(selected=True).order_by('created_at')[:4],
        'tags': Tag.objects.all(),
        'categories': Category.objects.all(),
        'category_slug': slug,
        'title': 'Allaia Blog &amp; News | ' + Category.objects.get(slug=slug).name,
        'current_page': page,
        'pages_count': math.ceil(len(posts) / 20.),
    })


@require_http_methods(('POST',))
@login_required
def leave_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    text = request.POST.get('text')

    if len(text) > 0:
        Comment.objects.create(
            user=request.user,
            blog=blog,
            text=text,
        ).save()

    return HttpResponseRedirect(reverse('blog:blog', kwargs={'pk': pk}))
