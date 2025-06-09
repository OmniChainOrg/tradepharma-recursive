# ds_bot/inventory/inventory.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='open', max_length=50)

class Demand(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='open', max_length=50)

class Match(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    demand = models.ForeignKey(Demand, on_delete=models.CASCADE)
    matched_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='pending', max_length=50)
