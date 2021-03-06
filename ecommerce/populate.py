import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

import lorem
import random
import argparse
from random import shuffle

import django
django.setup()

from django.core.files import File
from django.contrib.auth.models import User

from review.models import Review
from blog.models import Category, Tag, Blog, Comment
from product.models import Color, Product, Manufacturer, Image


tags = ['Food', 'Bars', 'Cooktails', 'Shops', 'Best', 'Offers', 'Transports', 'Restaurants']

categories = ['Food', 'Places to visit', 'New Places', 'Suggestions and guides']


def populate_product(num):
    for _ in range(num):

        colors = Color.objects.order_by('?')[:3]
        manufacturer = Manufacturer.objects.order_by('?')[0]
        images = list(Image.objects.order_by('?')[:7])
        shuffle(images)

        product = Product.objects.create(
            name=lorem.sentence(),
            short_description=lorem.paragraph() + '<br/>',
            full_description=''.join([f'<p> { lorem.paragraph() } </p>' for _ in range(random.randint(3, 7))]),
            price=random.randint(5, 30),
            availability=random.randint(0, 100),
            size='x'.join([str(random.randint(5, 20) * 10) for _ in range(3)]),
            weight=str(random.randint(5, 15) / 10) + 'kg',
            manufacturer=manufacturer,
        )
        product.colors.set(colors)
        product.images.set(images)
        product.save()

    for product in Product.objects.all():
        product.similar_to.set(Product.objects.order_by('?')[:5])
        product.save()


def populate_image(num, path='media/products'):
    images = [os.path.join('products', file) for file in os.listdir(path)
             if file.lower().endswith(('.jpg', '.png', '.jpeg'))]

    for i, image in enumerate(images[:num]):
        Image.objects.create(
            name=i,
            image=image,
        )


def populate_review(num):
    for product in Product.objects.all():
        for _ in range(num):
            Review.objects.create(
                user=User.objects.order_by('?')[0],
                product=product,
                rate=random.randint(0, 5),
                title=lorem.sentence()[:25],
                text=lorem.paragraph(),
            ).save()


def populate_tag(num):
    for tag in tags[:num]:
        Tag.objects.create(
            name=tag,
        ).save()


def populate_category(num):
    for category in categories[:num]:
        Category.objects.create(
            name=category,
        ).save()


def populate_blog(num, path='media/blog'):
    images = [os.path.join('blog', file) for file in os.listdir(path)
              if file.endswith(('.png', '.jpg', '.jpeg'))]
    for _ in range(num):
        blog = Blog.objects.create(
            user=User.objects.order_by('?')[0],
            category=Category.objects.order_by('?')[0],
            title=lorem.sentence(),
            main_image=random.choice(images),
            text=''.join([f'<p>{ lorem.paragraph() }</p>' for _ in range(random.randint(3, 10))])
        )
        blog.tags.set(Tag.objects.order_by('?')[:3])
        blog.save()


def populate_comment(num):
    for blog in Blog.objects.all():
        for _ in range(random.randint(1, num)):
            Comment.objects.create(
                user=User.objects.order_by('?')[0],
                blog=blog,
                text=''.join([f'<p>{ lorem.paragraph() }</p>' for _ in range(random.randint(1, 2))])
            ).save()


def main(args):
    if args.module == 'product':
        populate_product(args.quantity)
    elif args.module == 'product.image':
        populate_image(args.quantity)
    elif args.module == 'review':
        populate_review(args.quantity)
    elif args.module == 'blog':
        populate_blog(args.quantity)
    elif args.module == 'blog.tag':
        populate_tag(args.quantity)
    elif args.module == 'blog.category':
        populate_category(args.quantity)
    elif args.module == 'blog.comment':
        populate_comment(args.quantity)
    else:
        raise ValueError('No populate script for this module.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('module', type=str)
    parser.add_argument('quantity', type=int, default=int())
    args = parser.parse_args()
    main(args)
