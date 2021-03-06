import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

import lorem
import random
import argparse
from random import shuffle

import django
django.setup()

from django.core.files import File

from product.models import Color, Product, Manufacturer, Image


sneakers = ['UA HOVR™ Machina Running Shoes', 'HOKA Carbon X 2 Sneakers', 'Nike Space Hippie 04 Sneakers',
            'Nike Go FlyEase Sneakers', 'Nike Air Zoom Tempo NEXT% Sneakers', 'APL Superfuture Sneakers',
            'Puma FUSE Training Shoes', 'Taft The Jack Sneaker', 'Allen Edmonds Courtside Custom Sneakers',
            'Air Jordan XXXV Basketball Sneakers', 'Skechers GOrun Razor 3 Cloak Hyper', 'Koio Chukka Dune Sneakers',
            'Brooks Levitate 4 LE Sneakers', 'Converse Digital Terrain All Star Disrupt CX',
            'Adidas Ultraboost 21 Shoes', 'Brandblack Specter SuperCritical Runner',
            'Reebok Nano X1 Men\'s Training Shoes', 'PUMA Dreamer 2 Basketball Sneakers', 'Adidas Originals Superstar']


def populate_product(num):
    for name in sneakers[:num]:
        if Product.objects.filter(name=name).count():
            continue

        colors = Color.objects.order_by('?')[:3]
        manufacturer = Manufacturer.objects.order_by('?')[0]
        images = list(Image.objects.order_by('?')[:5])
        shuffle(images)
        similar_products = Product.objects.order_by('?')[:5]

        product = Product.objects.create(
            name=name,
            short_description=lorem.paragraph() + '<br/>',
            full_description=''.join(['<p>' + lorem.paragraph() + '</p>' for _ in range(5)]),
            price=random.randint(100, 300),
            availability=random.randint(0, 100),
            size='x'.join([str(random.randint(5, 20) * 10) for _ in range(3)]),
            weight=str(random.randint(5, 15) / 10) + 'kg',
            manufacturer=manufacturer,
        )
        product.colors.set(colors)
        product.images.set(images)
        product.similar_to.set(similar_products)
        product.save()


def populate_image(num, path='populate_data/images'):
    files = [os.path.join(path, file) for file in os.listdir(path)
             if file.lower().endswith(('.jpg', '.png', '.jpeg'))]

    for file in files[:num]:
        if not Image.objects.filter(name=file).count():
            image = Image.objects.create(name=file)
            print(file)
            image.image.save(file, File(open(file), 'rb'))  # TODO: Fix image upload
            image.save()


def main(args):
    if args.module == 'product':
        populate_product(args.quantity)
    elif args.module == 'product.image':
        populate_image(args.quantity)
    else:
        raise ValueError('No populate script for this module.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('module', type=str)
    parser.add_argument('quantity', type=int, default=int())
    args = parser.parse_args()
    main(args)
