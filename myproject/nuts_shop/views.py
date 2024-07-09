from django.shortcuts import render


def index(request):
    return render(request, 'nuts_shop/index.html')
