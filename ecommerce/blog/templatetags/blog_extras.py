from django import template
from blog.models import Comment, Blog

register = template.Library()


@register.filter
def short_title(title):
    output = ""
    for word in title.split():
        if len(output + word) < 30:
            output += word + ' '
    output += '...'
    return output


@register.filter
def intro(text):
    return text[:200] + '...</p>'


@register.filter
def comments_count(post):
    return Comment.objects.filter(blog=post).count()


@register.filter
def posts_count(category):
    return Blog.objects.filter(category=category).count()
