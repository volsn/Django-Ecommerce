from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey('blog.Category', on_delete=models.PROTECT)
    tags = models.ManyToManyField('blog.Tag')
    title = models.CharField(max_length=128)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    main_image = models.ImageField(upload_to='blog', blank=True, default='blog/default.png')

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    blog = models.ForeignKey('blog.Blog', on_delete=models.PROTECT)
    # reply_to = models.ForeignKey('blog.Comment', on_delete=models.PROTECT, blank=True) TODO: add reply functionality
    created_at = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=1024)
