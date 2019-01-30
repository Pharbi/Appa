# Hello command function
import discord

class Hello():

	def __init__(self, msg, bot):
		self.msg = msg
		self.bot = bot

	def hi(self):
		ctx = self.msg
		bot = self.bot
		
		if ctx.message.author == bot.user:
			return

		if ctx.message.content.startswith('!hello'):
			msg = 'Hello {0.author.mention}'.format(ctx.message)
			return msg