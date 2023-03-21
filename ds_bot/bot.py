import discord
from datetime import datetime
# from ds_bot.configs import config as cf
# from ds_bot.Quick_commands.command_module import on_message   # commend for test
from discord.ext import commands
# from ds_bot.models import *
# import ssl
import logging
# from ds_bot.models import DiscordUser
# from .models import *

# from ds_app import settings as st
# from marketplace.inventory imporaat Inventory, Product
# from marketplace.payment import process_payment
# import stripe
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# TOKEN = cf.TOKEN
TOKEN = 'MTA3NDE3MDgxNjU0MDk3NTE2NQ.GJz7LH.cEl2PC0wavAsaUby8sjjQgtnRDnKTkIR_qdfU8'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
# inventory = Inventory()
# stripe.api_key = "sk_test_XXXXXXXXXXXXXXXXXXXXXXXX"

# @client.event
# async def on_message(message):
#
#     if not message.author.bot and not message.content.startswith('!'):
#
#         discorduser, created = DiscordUser.objects.get_or_create(
#             user_id=message.author.id,
#             defaults={
#                 'username': message.author.name,
#                 'created_at': datetime.now()
#             }
#         )
#
#         # Сохраняем профиль пользователя
#         discorduser.save()
@client.event
async def on_ready():
    print("Bot is ready")

# @client.event
# async def on_message(message):
#     await on_message(message)

@client.command(pass_context=True)  # разрешаем передавать агрументы  }
async def test(ctx, arg):  # создаем асинхронную фунцию бота            } # TEST SETTING
    await ctx.send(arg)  # отправляем обратно аргумент             }

@client.command()          #              }
async def ping(ctx):  #                  }   TEST SETTING
    user = ctx.author
    logger.info("User %s (%s) started: %s", user.name, user.id, ctx.message.content)
    await ctx.send('pong')   #           }



# @client.command()
# async def order(ctx, item, quantity):
#     product = Inventory.find_product(item)
#     if product and product.stock >= int(quantity):
#         success = process_payment(int(quantity) * int(product.price * 100), "tok_visa")
#         if success:
#             Inventory.update_stock(item, product.stock - int(quantity))
#             await ctx.send(f"Order for {quantity} {item}(s) processed successfully")
#         else:
#             await ctx.send("Sorry, payment failed.")
#     else:
#         await ctx.send("Sorry, that item is out of stock or the quantity is not available.")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command")








#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command()
    async def add_product(self, ctx, name: str, price: float, stock: int):
        Product.objects.create(name=name, price=price, stock=stock)
        await ctx.send(f"Product {name} added to inventory.")

    @client.command()
    async def remove_product(self, ctx, name: str):
        Product.objects.filter(name=name).delete()
        await ctx.send(f"Product {name} removed from inventory.")

    @client.command()
    async def update_stock(self, ctx, name, new_stock: int):
        product = Product.objects.get(name=name)
        product.stock = new_stock
        product.save()
        await ctx.send(f"Stock updated for {name}.")

    @client.command()
    async def find_product(self, ctx, name):
        try:
            product = Product.objects.get(name=name)
            await ctx.send(f"{product.name}: {product.stock}")
        except Product.DoesNotExist:
            await ctx.send(f"Product {name} not found in inventory.")

    @client.command()
    async def display_inventory(self, ctx):
        inventory_list = []
        for product in Product.objects.order_by('name'):
            inventory_list.append(f"{product.name}: {product.stock}")
        inventory_str = "\n".join(inventory_list)
        await ctx.send(f"Current inventory:\n{inventory_str}")

# Create an instance of the Inventory cog and add it to the bot
inventory_cog = Inventory(client)
client.add_cog(inventory_cog)
client.run(TOKEN)