"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


handler404 = 'base.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    # TODO: Try to make it clear what the problem is in
    path('', include(('base.urls', 'base'))),  # , namespace='base_namespace'
    path('products/', include(('product.urls', 'product'))),  # namespace='product_namespace'
    path('blogs/', include(('blog.urls', 'blog'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
