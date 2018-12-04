import discord
from discord.ext import commands
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
    if ctx.message.author == bot.user:
        return

    if ctx.message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(ctx.message)
        await  ctx.send(msg)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)

