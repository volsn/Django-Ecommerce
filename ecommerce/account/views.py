from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from product.models import Product
from account.models import UserAccount
# Create your views here.


def login_register(request):
    return render(request, 'account/account.html', context={})


@require_http_methods(('POST',))
def user_login(request):

    email = request.POST.get('email')
    password = request.POST.get('password_in')

    user = authenticate(username=email, password=password)

    if user:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('base:index'))
        else:
            return HttpResponse('ACCOUNT NOT ACTIVE')
    else:
        return HttpResponse('LOGIN FAILED')


@require_http_methods(('POST',))
def user_register(request):

    user_fields = ('email', 'password', 'first_name', 'last_name',)
    account_fields = ('full_address', 'city', 'postal_code', 'country', 'telephone')

    pass  # TODO: Finish registration view using forms


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('base:index'))


@login_required
def like(request, pk):
    product = get_object_or_404(Product, pk=pk)
    account = get_object_or_404(UserAccount, user=request.user)
    account.liked.add(product)
    return HttpResponseRedirect(reverse('product:liked'))


@login_required
def unlike(request, pk):
    product = get_object_or_404(Product, pk=pk)
    account = get_object_or_404(UserAccount, user=request.user)
    account.liked.remove(product)
    return HttpResponseRedirect(reverse('product:liked'))


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    account = get_object_or_404(UserAccount, user=request.user)
    account.cart.add(product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    account = get_object_or_404(UserAccount, user=request.user)
    account.cart.remove(product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
