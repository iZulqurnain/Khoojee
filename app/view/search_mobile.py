from django.shortcuts import render


def mobile_home(request):
    return render(request, 'pages/mobile_search/home.html')


def mobile_search(request):
    return render(request, 'pages/search/index.html')