from django.shortcuts import render


def about_us(request):
    return render(request, 'pages/about_us/home.html')

