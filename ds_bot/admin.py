from django.contrib import admin
from .models import Item
from .models import Inventory
from .models import DiscordUser
from .models import InventoryItem


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_added']

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('inventory', 'item')


@admin.register(DiscordUser)
class DiscordUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'bot', 'created_date')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'date_added', 'user')




# Register your models here.
