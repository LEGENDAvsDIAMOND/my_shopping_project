from django.db import models

class Categ(models.Model):
    name = models.CharField(max_length=100)
