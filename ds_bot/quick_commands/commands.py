# # from django.db import models
# # from asgiref.sync import
# import discord
# import logging
# from discord.ext import commands
# from discord.ext import commands
# from asgiref.sync import sync_to_async
# from ds_bot.models import DiscordUser
# from ds_bot.models import *
#
#
# client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
#
#
# async def create_discord_user(message_author_id, message_author_name):
#     await sync_to_async(DiscordUser.objects.get_or_create)(
#         user_id=message_author_id,
#         defaults={
#             'name': message_author_name,
#         }
#     )
# # Используем асинхронную версию функции create_discord_user в событии on_message
# @client.event
# async def on_message(message):
#     if not message.author.bot and not message.content.startswith('!'):
#         message_author_id = message.author.id
#         message_author_name = message.author.name
#         await create_discord_user(message_author_id, message_author_name)
#     await client.process_commands(message)