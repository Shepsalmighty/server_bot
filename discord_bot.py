import asyncio
import discord
from discord import app_commands
from discord.ext import commands
import server_main
from BOT_TOKEN import BOT_TOKEN
# import pyotp
# import time
#
#
# totp =  pyotp.TOTP('base32secret3232')

#
# intents = discord.Intents.default()
# intents.message_content = True
# intents.guild_messages = True
#
# # intents.message_content.is_integer(1) ??????????
#
#
# client = discord.Client(intents=intents, id=1194339104305987654)
# tree = app_commands.CommandTree(client)
#
# bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
#
# # @client.event
# # async def on_ready():
# #     channel = client.get_channel(1194339105329389701)
# #     message = "message recieved"
# #     await channel.send(message)
# #     await bot.tree.sync()
#
# # @bot.slash_command(name="serverUp", description="server starting")
#
# # @bot.tree.command(
# #     name="server_up",
# #     description="Starting server"
# # )
#
# @bot.tree.command(
#     name="server_up",
#     description="Starting server"
# )
# # async def server_up(interaction: discord.Interaction):
# #     await interaction.response.send_message("Starting server")
# async def server_up(ctx):
#     await ctx.respond("starting server")
#
# @bot.event
# async def sync_commands(ctx):
#     bot.tree.sync()
#
#
#
# # @bot.tree.command(
# #     name="server_up",
# #     description="Starting server"
# # )
# #
# # def server_up():
# #     return server_main.ServerControls.serverUp()
#
# @client.event
# async def on_ready():
#     channel = client.get_channel(1194339105329389701)
#     message = "new message"
#     await channel.send(message)
#     await bot.tree.sync()
#
#     # await bot.tree.sync(guild=discord.Object(id=1194339104305987654))
#
# # @bot.command()
# # async def up(ctx: interaction.CommandContext):
# #     await ctx.send("command made")
#
# # @tree.command(
# #     name = "server_down",
# #     description = "Stopping server"
# # )
# # def serverDown():
# #     server_main.ServerControls.serverDown()
# #
# # @tree.command(
# #     name = "server_create",
# #     description = "Create new server"
# # )
# # def serverCreate():
# #     server_main.ServerControls.serverCreate()
# #
# # @tree.command(
# #     name = "serverDel",
# #     description= "Permanently deletes server"
# # )
# # def serverDel():
# #     server_main.ServerControls.serverDel()
# #
# # @tree.command(
# #     name = "serverExtend",
# #     description = "Extend automated shutdown by specified number of whole hours"
# # )
# # def serverExtend():
# #     pass
#
# # async def Up(ctx):
# #   await ctx.respond(f"Hello, {ctx.author}!")
#
#
#
#
# client.run(BOT_TOKEN)
# # bot.run(BOT_TOKEN)

intents = discord.Intents.all()
client = discord.Client(intents=intents, id=1194339104305987654)
tree = app_commands.CommandTree(client)
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.tree.command(name="server_up")
async def server_up(ctx):
    await ctx.respond("starting server")


@bot.event
async def on_ready():
    await bot.tree.sync()


bot.run(BOT_TOKEN)

# TODO: look down vvvv

raise NotImplemented("""ADD - TOTP (timed one time password) for 2FA for our bot, and make BOT_TOKEN
environment variable""")





