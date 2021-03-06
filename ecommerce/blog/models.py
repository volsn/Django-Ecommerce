from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey('blog.Category', on_delete=models.PROTECT)
    title = models.CharField(max_length=128)
    text = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    main_image = models.ImageField(upload_to='blog')

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    blog = models.ForeignKey('blog.Blog', on_delete=models.PROTECT)
    reply_to = models.ForeignKey('blog.Comment', on_delete=models.PROTECT, blank=True)
    created_on = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=1024)
