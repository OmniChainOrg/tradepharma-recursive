# ds_bot/models/inventory.py
from django.db import models
from .item import Item

class Inventory(models.Model):
    name = models.CharField(max_length=255)
    items = models.ManyToManyField(Item, through='InventoryItem')

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.inventory} - {self.item}"
