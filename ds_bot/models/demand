# ds_bot/models/demand.py
from django.db import models
from .product import Product

class Demand(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='open', max_length=255)

    def __str__(self):
        return f"Demand {self.id} for {self.product.name}"
