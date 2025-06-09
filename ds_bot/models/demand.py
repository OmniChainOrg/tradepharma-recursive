# ds_bot/models/demand.py
from django.db import models
from .item import Item

class Demand(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='open', max_length=255)

    def __str__(self):
        return f"Demand {self.id} for {self.item.name}"
