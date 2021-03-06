from django.db import models

# Create your models here.


class Color(models.Model):
    name = models.CharField(max_length=64, unique=True)
    hex_code = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    short_description = models.TextField()
    full_description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.IntegerField()
    colors = models.ManyToManyField('product.Color')
    # main_image = models.ForeignKey('product.Image', on_delete=models.CASCADE)
    images = models.ManyToManyField('product.Image', blank=True)
    size = models.CharField(max_length=16)
    weight = models.CharField(max_length=8)
    manufacturer = models.ForeignKey('product.Manufacturer', on_delete=models.PROTECT)
    similar_to = models.ManyToManyField('product.Product', blank=True)

    top_selling = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    @property
    def price_display(self):
        return f"${ self.price }"

    def __str__(self):
        return self.name
