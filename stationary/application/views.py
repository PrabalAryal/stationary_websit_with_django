from django.shortcuts import render
import pymongo
import bcrypt
from pymongo import MongoClient
from .models import stationaryitems
from django.http import HttpResponseRedirect
from .models import register_info
from django.http import HttpResponse
from django.contrib.auth import authenticate
import base64

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["stationary"]


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


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        collection = db["collection4"]

        user = collection.find_one({"email": email})

        if user:
            hashed_password = base64.b64decode(user["password"])
            if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
                # he bcrypt.checkpw function expects both arguments to be bytes objects.#The first argument is the plaintext password entered by the user, which is a string. The encode method #is used to convert this string into a bytes object.#The second argument is the hashed password retrieved from the database. If you're storing the hashed #password as a base64-encoded string, you need to use base64.b64decode to decode it into a bytes object.So, even though both the plaintext password and the hashed password are originally strings, they need #to be converted to bytes objects before they can be passed to bcrypt.checkpw. This is why you see both #encode and base64.b64decode being used.
                return HttpResponseRedirect("http://127.0.0.1:8000/")
            else:
                return HttpResponse("wrong credentials")

    return render(request, "login.html")


# Create your views here.
