import discord
from discord.ext import commands
from commands import hello as hello_CMD
from commands import yipyip as yip_yip_CMD
import os
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
async def hello(ctx):
    send = hello_CMD.Hello(ctx, bot)
    resp = send.hi()
    await ctx.send(resp)

@bot.command()
async def commands(ctx):
    if ctx.message.content.startswith('!commands'):
        msg = 'Currently my only commands are the ability to say hello and send random gifs. Try now with the !hello command or !yipyip '.format(ctx.message)
        await ctx.send(msg)

@bot.command()
async def yipyip(ctx):
    send = yip_yip_CMD.YipYip(ctx, bot)
    resp = send.giphy()
    await ctx.send(resp)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)

