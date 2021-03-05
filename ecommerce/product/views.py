from django.shortcuts import render
from product.models import Product

# Create your views here.


def products(request):
    return render(request, 'base/listing-grid-1-full.html', context={'products': Product.objects.all()[:20]})
