from django.db import models

# Create your models here.

class StockList(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    fullname = models.CharField(max_length=100)
    intename = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    starttime = models.DateField()
    location = models.CharField(max_length=10)
    province = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    industry = models.CharField(max_length=10)
    www = models.CharField(max_length=50)
