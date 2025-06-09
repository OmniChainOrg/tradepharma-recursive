from django.contrib import admin
from .models import Item
from .models import Inventory
from .models import InventoryItem


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_added')
    list_filter = ('user',)
    search_fields = ('user__name',)

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('inventory', 'item')
    list_filter = ('inventory', 'item')
    search_fields = ('inventory__user__name', 'item__name')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'date_added', 'user')
    list_filter = ('user', 'available')
    search_fields = ('name',)




# Register your models here.
