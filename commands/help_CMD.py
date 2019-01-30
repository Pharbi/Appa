# help command !commands invocation
import os

dir = os.listdir("commands")



class Commands():

	def __init__(self, msg, bot):
		self.msg = msg
		self.bot = bot

	def list(self):
		msg = "Here are a list of live Appa bot commands: \n"
		for cmd in dir:
			
			
			if (cmd == 'help_CMD.py') or (cmd == '__pycache__'):
				continue
			else:
				cmd = cmd[:-3]
				msg += "**!" + cmd + "**\n"
		return msg

	def description(self):
		ctx = self.msg
		bot = self.bot

		if ctx.message.author == bot.user:
			return
		else:
			msg = "**!commands**: \nprovides a list available commands currently live for Appa bot"
			return msg