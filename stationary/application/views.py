from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def items(request):
    return render(request, "items.html")


def buy(request):
    return render(request, "buy.html")


def sell(request):
    return render(request, "sell.html")


def about(request):
    return render(request, "about.html")


# def contact(request):
#   return render(request, "contact.html")
