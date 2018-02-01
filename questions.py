from discord.ext import commands
from random import choice, shuffle
import aiohttp
import functools
import asyncio

class query:
    def __init__(self,bot):
        self.bot = bot

@commands.group(name="question", no_pm=True,pass_context=True)
async def getquestion(self,ctx):
    """Built in Helpdesk style ticketing syste for questions"""
    await self.bot.send_cmd_help(ctx)

@getquestion.command(pass_context=True, name="question")
