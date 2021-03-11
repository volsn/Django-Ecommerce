import math

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from review.models import Review
from product.models import Product
from account.models import UserAccount

# Create your views here.


def products(request):

    page = int(request.GET.get('page', 0))
    products_ = Product.objects.order_by('?')

    return render(request, 'product/listing-grid-1-full.html', context={
        'products': products_[page*12:(page+1)*12],
        'current_page': page,
        'pages_count': math.ceil(len(products_) / 12.),
    })


def product(request, pk):

    product_obj = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product_obj).order_by('updated_on')[:4]

    return render(request, 'product/product-detail-2.html', context={'product': product_obj, 'reviews': reviews})


@login_required
def liked_products(request):

    account = get_object_or_404(UserAccount, user=request.user)
    page = int(request.GET.get('page', 0))
    products_ = account.liked.order_by('?')

    return render(request, 'product/listing-row-1-sidebar-left.html', context={
        'products': products_[page*12:(page+1)*12],
        'current_page': page,
        'pages_count': math.ceil(len(products_) / 12.),
    })
