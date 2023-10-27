from django.db import models
from categ.models import Categ

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categ, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()