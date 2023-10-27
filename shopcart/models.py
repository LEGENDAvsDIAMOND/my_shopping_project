from django.db import models
from main_cus.models import MainCus

class ShopCart(models.Model):
    date = models.DateField()
    owner = models.ForeignKey(MainCus, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.CharField(max_length=100)
