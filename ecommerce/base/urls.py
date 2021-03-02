from django.urls import path
from base import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.error, name='error')
]
