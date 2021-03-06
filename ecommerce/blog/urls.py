from django.urls import path
from blog import views

urlpatterns = [
    path('all/', views.all_blogs, name='all'),
    path('<int:pk>/', views.blog_view, name='blog'),
    path('<str:slug>/', views.category, name='category')
]
