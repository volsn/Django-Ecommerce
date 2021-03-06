from django.shortcuts import render
from blog.models import Blog
from product.models import Product

# Create your views here.


def index(request):
    return render(request, 'base/index.html', context={
        'blogs': Blog.objects.filter(selected=True).order_by('created_at')[:4],
        'top_sellings': Product.objects.filter(top_selling=True)[:8],
        'featured': Product.objects.filter(featured=True)[:6],
    })


def handler404(request, exception):
    return render(request, 'base/404.html', status=404)


def about(request):
    return render(request, 'base/about.html')


def contacts(request):
    return render(request, 'base/contacts.html')


def help_(request):
    return render(request, 'base/help.html')
