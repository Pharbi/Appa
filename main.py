import discord
import os
from discord.ext import commands
from commands import hello as hello_CMD
from commands import yipyip as yip_yip_CMD
from commands import help_CMD
from os.path import join, dirname
from dotenv import load_dotenv
'''
    APPA BOT for Discord, currently in short version
    Looking forward to adding more features later

'''
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command()
async def hello(ctx, *args):
    send = hello_CMD.Hello(ctx, bot)

    if "desc" in args:
        resp = send.description()
    else:
        resp = send.hi()
    await ctx.send(resp)

@bot.command()
async def commands(ctx, *args):
    send = help_CMD.Commands(ctx, bot)
    
    if "desc" in args:
        resp = send.description()
        
    else:
        resp = send.list()
        resp += "add 'desc' to any of the commands to find out more!"
    await ctx.send(resp)

@bot.command()
async def yipyip(ctx, *args):
    send = yip_yip_CMD.YipYip(ctx, bot)

    if "desc" in args:
        resp = send.description()
    else: 
        resp = send.giphy()
    await ctx.send(resp)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)

