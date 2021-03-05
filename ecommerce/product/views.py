from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from product.models import Product

# Create your views here.


def products(request):
    return render(request, 'product/listing-grid-1-full.html', context={'products': Product.objects.all()[:20]})


def product(request, pk):
    """
    try:
        product_obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return reverse('base:handler404')
    """
    product_obj = get_object_or_404(Product, pk=pk)

    return render(request, 'product/product-detail-2.html', context={'product': product_obj})
