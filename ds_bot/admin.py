# ds_bot/admin.py

from django.contrib import admin
from ds_bot.models import Item, Inventory

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



# Register your models here.
