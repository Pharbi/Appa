# Creating random giphy stuff, with !yipyip command
import discord
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import os
from os.path import join, dirname
from dotenv import load_dotenv
import json 

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

class YipYip():

	def __init__(self, msg, bot):
		self.msg = msg
		self.api_key = os.getenv('GIPHY')
		self.bot = bot

	def giphy(self):
		ctx = self.msg
		bot = self.bot
		api = giphy_client.DefaultApi()
		api_key = self.api_key
		tag = 'avatar the last airbender'
		fmt = 'json' # Currently json but I should figure out a way to just get a url - kay

		if ctx.message.author == bot.user:
			return
		elif ctx.message.content.startswith('!yipyip'):
			try:
				api_resp = api.gifs_random_get(api_key, tag=tag, fmt=fmt)
				giphy_url = api_resp.data.image_original_url
				return giphy_url
				
			except ApiException as exception:
				# Send error response to chat, will soon link an online dev
				msg = "Unable to get random gif: ".append(exception + "\n")
				print(msg)
				return msg