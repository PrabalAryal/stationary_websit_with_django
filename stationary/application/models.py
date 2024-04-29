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
