# import os
# import discord
# from discord.ext import commands
# import django
# from ds_bot.models import *
# client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
# # # Configure the Django project and settings module
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
# # django.setup()
#
#
# class Inventory(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#
#     @commands.command()
#     async def add_product(self, ctx, name: str, price: float, stock: int):
#         Product.objects.create(name=name, price=price, stock=stock)
#         await ctx.send(f"Product {name} added to inventory.")
#
#     @commands.command()
#     async def remove_product(self, ctx, name: str):
#         Product.objects.filter(name=name).delete()
#         await ctx.send(f"Product {name} removed from inventory.")
#
#     @commands.command()
#     async def update_stock(self, ctx, name, new_stock: int):
#         product = Product.objects.get(name=name)
#         product.stock = new_stock
#         product.save()
#         await ctx.send(f"Stock updated for {name}.")
#
#     @commands.command()
#     async def find_product(self, ctx, name):
#         try:
#             product = Product.objects.get(name=name)
#             await ctx.send(f"{product.name}: {product.stock}")
#         except Product.DoesNotExist:
#             await ctx.send(f"Product {name} not found in inventory.")
#
#     @commands.command()
#     async def display_inventory(self, ctx):
#         inventory_list = []
#         for product in Product.objects.order_by('name'):
#             inventory_list.append(f"{product.name}: {product.stock}")
#         inventory_str = "\n".join(inventory_list)
#         await ctx.send(f"Current inventory:\n{inventory_str}")
#
#
#
#
#
#

