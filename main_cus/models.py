from django.db import models

class MainCus(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    date = models.DateField()
