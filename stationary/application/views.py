from django.shortcuts import render
import pymongo
from pymongo import MongoClient
from .models import stationaryitems
from django.http import HttpResponseRedirect
from .models import register_info


# Create your views here.
def home(request):
    return render(request, "home.html")


def items(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["stationary"]
    collection = db["collection1"]
    sold_items = collection.find()
    return render(request, "items.html", {"sold_items": sold_items})


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


def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        register_info.register(username, email, password)
        return HttpResponseRedirect("http://127.0.0.1:8000/")

    return render(request, "signup.html")


# Create your views here.
