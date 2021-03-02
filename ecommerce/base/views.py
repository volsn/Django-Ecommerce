from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'base/index.html', context={})


def error(request):
    return render(request, 'base/404.html', context={})
