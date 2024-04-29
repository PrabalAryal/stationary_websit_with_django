from django.shortcuts import render
import pymongo
from pymongo import MongoClient
from .models import stationaryitems
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request, "home.html")


def items(request):
    return render(request, "items.html")


def buy(request):
    return render(request, "buy.html")


def sell(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")

        stationaryitems.product(product_name, price, quantity)

        return HttpResponseRedirect("/success/")

    return render(request, "sell.html")


def about(request):
    return render(request, "about.html")


# Create your views here.
