import statistics
from django import template

register = template.Library()


@register.filter
def range_(value, empty: bool = True) -> range:
    return range(5-int(value)) if empty else range(int(value))


@register.filter
def avg_rate(reviews):
    return round(statistics.mean([review.rate for review in reviews]), 1)


@register.filter
def time(value):
    return value
