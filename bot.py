import discord
from discord.ext import commands, tasks
import requests
import time
import pypi
import json
import os
import re

PATH = os.path.dirname(os.path.abspath(__file__))
API_BASE_URL = "https://pypi.python.org/pypi/"
PACKAGE_LIST_PATH = f"{PATH}/all_packages.json"


bot = commands.Bot(command_prefix="p!")


@bot.command()
async def register(ctx, project_name):
    pypi.get_package(project_name)
