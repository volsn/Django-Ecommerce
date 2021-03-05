from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'base/index.html', context={})


def handler404(request, exception):
    return render(request, 'base/404.html', status=404)
