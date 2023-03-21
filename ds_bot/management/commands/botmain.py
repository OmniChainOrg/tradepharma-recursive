
from django.core.exceptions import ValidationError

from django.core.management.base import BaseCommand

import discord

# from ds_bot.configs import config as cf
# from ds_bot.Quick_commands.command_module import on_message   # commend for test
from discord.ext import commands
import ssl
import logging
# from ds_bot.models import DiscordUser
from ds_bot.models import *
from asgiref.sync import sync_to_async

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# TOKEN = cf.TOKEN
TOKEN = 'MTA3NDE3MDgxNjU0MDk3NTE2NQ.G-_Mme.XoxfXilS77_eY1tbuSr8iugEF4vIGQCZxgou4Q'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
# inventory = Inventory()
# stripe.api_key = "sk_test_XXXXXXXXXXXXXXXXXXXXXXXX"

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()          #              }
async def ping(ctx):  #                  }   TEST SETTINGclear
    user = ctx.author
    logger.info("User %s (%s) started: %s", user.name, user.id, ctx.message.content)
    await ctx.send('pong')   #           }
#

@client.command(pass_context=True)  # разрешаем передавать агрументы  }
async def test(ctx, arg):  # создаем асинхронную фунцию бота            } # TEST SETTING
    await ctx.send(arg)  # отправляем обратно аргумент
    #        }

async def create_discord_user(message_author_id, message_author_name, message_author_discriminator):
    await sync_to_async(DiscordUser.objects.get_or_create)(
        user_id=message_author_id,
        defaults={
            'name': message_author_name,
            'bot': message_author_discriminator,

        }
    )

@client.event
async def on_message(message):
    if not message.author.bot and not message.content.startswith('!'):
        message_author_id = message.author.id
        message_author_name = message.author.name
        message_author_bot = message.author.bot
        await create_discord_user(message_author_id, message_author_name, message_author_bot)
    await client.process_commands(message)

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


class Command(BaseCommand):
    help = 'bot'


@client.command()
async def add_item(ctx):
    await ctx.send('Please enter the name of the new item:')
    name_msg = await client.wait_for('message',
                                     check=lambda msg: msg.author == ctx.author and msg.channel == ctx.channel)

    await ctx.send('Please enter the price of the new item:')
    price_msg = await client.wait_for('message',
                                      check=lambda msg: msg.author == ctx.author and msg.channel == ctx.channel)

    await ctx.send('Please enter the quantity of the new item:')
    stock_msg = await client.wait_for('message',
                                      check=lambda msg: msg.author == ctx.author and msg.channel == ctx.channel)


    try:
        # inventory = await sync_to_async(Inventory.objects.get_or_create)(
        #     user=ctx.author,
        #     quantity=int(stock_msg.content)
        # )[0]
        item = await sync_to_async(Item.objects.create)(
            name=name_msg.content.strip().title(),
            price=float(price_msg.content),
            stock=int(stock_msg.content),
            user=ctx.author.name
        )
        if stock_msg.content != 0 and price_msg.content != 0:
            await ctx.send(f'The "{item.name}" added to inventory {ctx.author.name}')
        else: await ctx.send('Wrong data, pls check you input data')
    except(ValueError, ValidationError):
        await ctx.send('Wrong data')
        return

@client.command()
async def find_item(ctx):
    await ctx.send('Please enter the name of the item:')
    item_msg = await client.wait_for('message',
                                     check=lambda msg: msg.author == ctx.author and msg.channel == ctx.channel)
    try:
        item = await sync_to_async(Item.objects.get)(name=item_msg.content.strip().title())
        await ctx.send(f"The price for {item.name} is {item.price} and the stock is {item.stock}, this item was created from {item.user}")
    except Item.DoesNotExist:
        await ctx.send('Item not found')


@client.command()
async def delete_item(ctx):
    await ctx.send('Please enter the name of the item to delete:')
    name_msg = await client.wait_for('message', check=lambda msg: msg.author == ctx.author and msg.channel == ctx.channel)

    try:
        item = await sync_to_async(Item.objects.get)(name=name_msg.content.strip().title(), user=ctx.author.name, is_deleted=False)
        item.is_deleted = True
        item.save()
        await ctx.send(f'The "{item.name}" has been removed from inventory {ctx.author.name}')
    except Item.DoesNotExist:
        await ctx.send(f'The item "{name_msg.content.strip().title()}" not found in your inventory')
    except Exception as e:
        await ctx.send(f'Done! but/')

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class Inventory(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#
#     @client.command()
#     async def add_product(self, ctx, name: str, price: float, stock: int):
#         Product.objects.create(name=name, price=price, stock=stock)
#         await ctx.send(f"Product {name} added to inventory.")
#
#     @client.command()
#     async def remove_product(self, ctx, name: str):
#         Product.objects.filter(name=name).delete()
#         await ctx.send(f"Product {name} removed from inventory.")
#
#     @client.command()
#     async def update_stock(self, ctx, name, new_stock: int):
#         product = Product.objects.get(name=name)
#         product.stock = new_stock
#         product.save()
#         await ctx.send(f"Stock updated for {name}.")
#
#     @client.command()
#     async def find_product(self, ctx, name):
#         try:
#             product = Product.objects.get(name=name)
#             await ctx.send(f"{product.name}: {product.stock}")
#         except Product.DoesNotExist:
#             await ctx.send(f"Product {name} not found in inventory.")
#
#     @client.command()
#     async def display_inventory(self, ctx):
#         inventory_list = []
#         for product in Product.objects.order_by('name'):
#             inventory_list.append(f"{product.name}: {product.stock}")
#         inventory_str = "\n".join(inventory_list)
#         await ctx.send(f"Current inventory:\n{inventory_str}")
#
# # Create an instance of the Inventory cog and add it to the bot
# inventory_cog = Inventory(client)
# client.add_cog(inventory_cog)
client.run(TOKEN)