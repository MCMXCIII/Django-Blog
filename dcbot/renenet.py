import discord
import asyncio
import requests


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

@client.event
BTCprice = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'
data = requests.get(BTCpriceurl).json()
BTCusd = data['USD']
async def on_message(message):
    if message.content.startswith('!pricebtc'):
        await client.edit_message(tmp, "The price of BTC is currently " + .format(requests.post(data=data))


client.run('NDAxMDMzMjA0OTg0ODQwMjEy.DTkX2w.cEiIbJvO1gyg3I0wQG0-cg87uYk')
