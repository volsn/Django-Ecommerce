from django import template

register = template.Library()


@register.filter
def total_price(products, extra=0):
    return sum([prd.price for prd in products]) + extra
