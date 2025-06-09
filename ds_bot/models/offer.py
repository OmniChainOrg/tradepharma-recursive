# ds_bot/models/offer.py
from django.db import models
from .item import Item

class Offer(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    status = models.CharField(default='open', max_length=50)

    def __str__(self):
        return f"{self.item.name} - {self.quantity}"
