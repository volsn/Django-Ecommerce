from django.urls import path
from account import views

urlpatterns = [
    path('', views.login_register, name='login_register'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='user_logout'),
]
