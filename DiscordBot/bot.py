# bot.py
import os
import discord

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

import importlib.util
spec = importlib.util.spec_from_file_location("bees", "commands/bee_movie.py")
bee_movie = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bee_movie)

test = importlib.util.spec_from_file_location("ball", "commands/magic_8_ball.py")
magic = importlib.util.module_from_spec(test)
test.loader.exec_module(magic)

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

    if message.content.partition(' ')[0] == '!8ball':
        await magic.ball(message)

    if message.content == '!bees':
        await bee_movie.bees(message)

client.run(TOKEN)
