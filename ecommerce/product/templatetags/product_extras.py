import statistics
from django import template
from django.shortcuts import get_object_or_404

from review.models import Review
from account.models import UserAccount

register = template.Library()


@register.filter
def range_(value, empty: bool = True) -> range:
    return range(5-int(value)) if empty else range(int(value))


@register.filter
def avg_rate(reviews):
    return round(statistics.mean([review.rate for review in reviews]), 1)


@register.filter
def get_reviews(product):
    return Review.objects.filter(product=product)


@register.filter
def range_pages(count):
    return range(count)


@register.filter
def is_in_cart(product, user):
    account = get_object_or_404(UserAccount, user=user)
    print(account.cart.filter(product=product))
    return account.cart.filter(product=product).exists()
