# from discord.ext import commands
# import discord
# from .models import DiscordUser
# client = commands.Bot(command_prefix='=', intents=discord.Intents.all())
#
# @client.event
# async def on_message(message):
#     # create obj and save in db
#     user = DiscordUser.objects.get_or_create(
#         user_id=message.author.id,
#         defaults={
#             'name': message.author.name,
#         },
#         # discord_tag=message.author.discriminator,
#         # locale=message.author.locale,
#         last_login=message.created_at,
#     )
#     # continue
#     # await client.process_commands(message)