from django.db import models
from django.utils.timezone import now

from datetime import datetime

class DiscordUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(verbose_name='Discord nickname', max_length=120)
    bot = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'#{self.user_id} #{self.name}'

    class Meta:
        verbose_name = 'Full User Info'
        verbose_name_plural = 'Full User Info'


class Inventory(models.Model):
    # owner = models.CharField(
    #     max_length=255
    # )
    user = models.ForeignKey(
        DiscordUser,
        on_delete=models.CASCADE,
        related_name='inventory'
    )
    date_added = models.DateTimeField(default=now, editable=False)
    items = models.ManyToManyField('ds_bot.Item', through='ds_bot.InventoryItem', related_name='inventories')
    # discord_user = models.OneToOneField(DiscordUser, on_delete=models.CASCADE, related_name='inventory')

    class Meta:
        verbose_name = 'inventory settings'
        verbose_name_plural = 'indicate inventory'

    def __str__(self):
        return f'Inventory #{self.user}'

class InventoryItem(models.Model):
    inventory = models.ForeignKey('ds_bot.Inventory', on_delete=models.CASCADE)
    item = models.ForeignKey('ds_bot.Item', on_delete=models.CASCADE)
    def __str__(self):
        return f' #{self.item}'


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=255, blank=True)
    available = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'







