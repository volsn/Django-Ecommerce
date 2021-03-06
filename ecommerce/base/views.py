from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'base/index.html')


def handler404(request, exception):
    return render(request, 'base/404.html', status=404)


def about(request):
    return render(request, 'base/about.html')


def contacts(request):
    return render(request, 'base/contacts.html')


def help(request):
    return render(request, 'base/help.html')
