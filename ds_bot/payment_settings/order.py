import discord
from discord.ext import commands
from ds_bot.models import *
from payment import process_payment

inventory = Inventory()

bot = commands.Bot(command_prefix="=", intents=discord.Intents.all())

# Define a command to process orders
@bot.command()
async def order(ctx, item: str, quantity: int):
    try:
        product = Product.objects.get(name=item)
        if product.stock >= quantity:
            # Process payment
            await process_payment(quantity * product.price, "tok_visa") # replace with a valid token
            # Update inventory
            product.stock -= quantity
            product.save()
            # Send confirmation message
            await ctx.send(f"Order for {quantity} {item}(s) processed successfully")
        else:
            await ctx.send("Sorry, that item is out of stock or the quantity is not available.")
    except Product.DoesNotExist:
        await ctx.send("Sorry, that item is not available in our inventory.")