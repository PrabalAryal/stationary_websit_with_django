from django.db import models
import pymongo
from pymongo import MongoClient


# Create your models here.
class stationaryitems(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()

    @staticmethod
    def product(product_name, price, quantity):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["stationary"]
        collection = db["collection1"]
        collection.insert_one(
            {"product_name": product_name, "price": price, "quantity": quantity}
        )
        client.close()


class productsstock(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    @staticmethod
    def product(product_name, quantity):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["stationary"]
        collection = db["collection2"]
        collection.insert_one({"product_name": product_name, "quantity": quantity})
        client.close()


# Path: stationary/application/views.py
# class login_info(models.Model):
#   username = models.CharField(max_length=100)
#  password = models.CharField(max_length=100)

# @staticmethod
# def login(username, password):
#   client = pymongo.MongoClient("mongodb://localhost:27017/")
#  db = client["stationary"]
# collection = db["collection3"]
# collection.insert_one({"username": username, "password": password})
# client.close()


class register_info(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    @staticmethod
    def register(username, email, password):
        print(f"username: {username}, email: {email}, password: {password}")
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["stationary"]
        collection_login = db["collection4"]
        collection_login.insert_one(
            {"username": username, "email": email, "password": password}
        )
        client.close()
