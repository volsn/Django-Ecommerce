import statistics
from django import template
from review.models import Review

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
