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

#using cryptocompare.
@bot.command()
async def owobot(coin):
    coinurl = "https://min-api.cryptocompare.com/data/price?fsym=" + coin.upper() + "&tsyms=USD"
    #Just realised formatting will be bad. Will fix this later.
    with urllib.request.urlopen(coinurl) as url:
        data = json.loads(str(url.read().decode()))
        coinresponse = (coin, [data][0]['USD'])
        await bot.say("This bot only prints in U.S. Dollars.")
        await bot.say(coinresponse)


@bot.command()
async def cmdhelp():
    await bot.say("Currently 3 commands.")
    await bot.say("owobot with a '!' as a prefix while adding the 3 Letter code for the coin.")
    await bot.say("ex. '!owobot XMR'. ")
    await bot.say("Then there is '!whenkonig' to tell you how much of a coin you would need to buy a brand new Koenigsegg. ")
    await bot.say("!info is a command that will give generic info about the OWO platform.")
    await bot.say("If you have a question about something and no one is around to awnser it use !question and the topic of your question and someone will get back to you. ")

@bot.command()
async def whenkonig(coin):
    coinurl = "https://min-api.cryptocompare.com/data/price?fsym=" + coin.upper() + "&tsyms=USD"
    #Just realised formatting will be bad. Will fix this later.
    with urllib.request.urlopen(coinurl) as url:
        data = json.loads(str(url.read().decode()))
        koniggrepo = (coin, 2100000 / [data][0]['USD'])
        await bot.say("You would need.")
        await bot.say(koniggrepo)
        await bot.say("To buy a brand new Koenigsegg.")

@bot.command()
async def info():
    await bot.say("This is for more information on anything you want information for.")
    await asyncio.sleep(5)
    await bot.say("After a short delay the bot will print information on anything you want.")
    await asyncio.sleep(5)
    await bot.say("the delay can be removed as well if you just want, to give one big post.")
    await asyncio.sleep(5)
    await bot.say("Just let me know how you would like this to be setup.")


#Start of tipping feature/command using https://blockchain.info/api.
@bot.command()
async def tip(user):
    await bot.say("Sending a tip to "+user)

@bot.command()
async def question(q):
    await bot.say("I don't have an awnser for that. I'll ask someone on the team and then get back to you.")
    velma = discord.utils.get(bot.get_all_members(), id='101872879649456128')
    owoman = discord.utils.get(bot.get_all_members(),id = '383127210690740226')
    if velma and owoman is not None:
        await bot.send_message(velma,"Someone has a question about: " + q)
        await bot.send_message(owoman,"Someone has a question about: " + q)
    else:
        bot.say("Message not sent.")


bot.run('NDAxMDMzMjA0OTg0ODQwMjEy.DTkX2w.cEiIbJvO1gyg3I0wQG0-cg87uYk')
