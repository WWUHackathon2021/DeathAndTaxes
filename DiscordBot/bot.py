# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


#RESPOND TO MASSAGES HERE
@client.event
async def on_message(message):
    #prevents bot from responding to self
    if message.author == client.user:
        return

    #test
    if message.content == '!test':
        response = "testing testing 1 2 3"
        await message.channel.send(response)

    #test2
    if message.content == '!pizzathehut':
        response = "nobody. outpizzas. the hut."
        await message.channel.send(response)

client.run(TOKEN)
