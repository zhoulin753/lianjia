from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=100)
    houseinfo = models.CharField(max_length=10)
    area = models.CharField(max_length=10)
    finish = models.CharField(max_length=10)
    house_type = models.CharField(max_length=30)
    floor = models.CharField(max_length=50)
    address = models.CharField(max_length=20)
    cost = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    url = models.CharField(max_length=100)