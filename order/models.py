from django.db import models
from store.models import *
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True, max_length=200)
    zipcode = models.CharField(max_length=100, null=True)
    
    city = models.CharField(max_length=100, null=True)
    paid = models.BooleanField(default=False)
    paid_amount = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.first_name


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name="items")
    market_price = models.FloatField(null=True)
    sale_price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.id)