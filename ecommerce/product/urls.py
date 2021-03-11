from django.urls import path
from product import views

urlpatterns = [
    path('all/', views.products, name='all'),
    path('liked/', views.liked_products, name='liked'),
    path('<int:pk>/', views.product, name='product'),
]
