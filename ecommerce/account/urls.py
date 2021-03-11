from django.urls import path
from account import views

urlpatterns = [
    path('', views.login_register, name='login_register'),
    path('like/<int:pk>/', views.like, name='like'),
    path('unlike/<int:pk>/', views.unlike, name='unlike'),
    path('cart/add/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>', views.remove_from_cart, name='remove_from_cart'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='user_logout'),
]
