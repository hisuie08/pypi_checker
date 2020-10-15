import discord
from discord.ext import commands, tasks
import requests
import time
import pypi
import json
import os
import re

TOKEN_PATH = os.path.dirname(os.path.abspath(__file__))+"/token.txt"
with open(TOKEN_PATH) as r:
    token = r.read()

bot = commands.Bot(command_prefix="p!")


@bot.command()
async def register(ctx, project_name):
    pypi.get_package(project_name).register()


bot.run(token)
