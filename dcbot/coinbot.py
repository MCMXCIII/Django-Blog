import requests
import urllib.request, json
import discord
from discord.ext import commands
import asyncio


bot = commands.Bot(command_prefix='!')
#Use the 3 char Abbrv for the coin to be used.
@bot.event
async def on_ready():
    print('Bot Ready!')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def getcoindata(coin):
    coinurl = "https://min-api.cryptocompare.com/data/price?fsym=" + coin + "&tsyms=USD"
    with urllib.request.urlopen(coinurl) as url:
        data = json.loads(str(url.read().decode()))
        coinresponse = (coin, [data][0]['USD'])
        await bot.say(coinresponse)
        #return print(coin, [data][0]['USD'])
        #await bot.say(print(str(coin+ " Is currently at " + [data][0]['USD'] + " USD")))
        #await bot.say(print([data][0]['USD']))


bot.run('NDAxMDMzMjA0OTg0ODQwMjEy.DTkX2w.cEiIbJvO1gyg3I0wQG0-cg87uYk')
