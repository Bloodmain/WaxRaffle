from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main.html',
                  {'title': 'WaxRaffle',
                   'selected': 0})


def purchase(request):
    return render(request, 'purchase.html',
                  {'title': 'Purchase',
                   'selected': 1})
