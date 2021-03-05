from django.urls import path
from product import views

urlpatterns = [
    path('all', views.products, name='all'),
    path('<int:pk>', views.product, name='product'),
]
