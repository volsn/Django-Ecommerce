from django.contrib import admin
from blog.models import Blog, Category, Tag, Comment

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
