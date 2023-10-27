from django.db import models
from products.models import Products
from shopcart.models import ShopCart

class Item(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    shopcart_id = models.ForeignKey(ShopCart, on_delete=models.CASCADE)
    sell_date = models.DateField()
