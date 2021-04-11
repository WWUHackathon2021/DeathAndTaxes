# bot.py
import os
import discord

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

import importlib.util
import random

spec = importlib.util.spec_from_file_location("bees", "commands/bee_movie.py")
bee_movie = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bee_movie)

spec = importlib.util.spec_from_file_location("ball", "commands/magic_8_ball.py")
magic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(magic)

spec = importlib.util.spec_from_file_location("csgo", "commands/counterstrike.py")
play = importlib.util.module_from_spec(spec)
spec.loader.exec_module(play)

doc = importlib.util.spec_from_file_location("accident", "commands/days_since_accident.py")
days = importlib.util.module_from_spec(doc)
doc.loader.exec_module(days)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

thieyreChecker = ["There", "Their", "They're"]
thieyreList = ["Sorry dumbass, I think you meant ""their're"".", "Sorry shitter, I think you meant ""theyre   '"".", "Sorry dogwater sage main, I think you meant ""thiare"".",
"ACTUALLY?! It's PRONOUNCED ""thir"".", "aha i think u meant tere", "uwu u silly its theri"]


#RESPOND TO MESSAGES HERE
@client.event
async def on_message(message):
    #prevents bot from responding to self
    if message.author == client.user:
        return

    #test
    if message.content == '!test':
        response = "testing testing 1 2 3"
        await message.channel.send(response)
    elif message.content.partition(' ')[0] == '!8ball':
        await magic.ball(message)
    elif message.content.partition(' ')[0] == '!track' or message.content.partition(' ')[0] == '!reset' or message.content.partition(' ')[0] == '!check':
        await days.accident(message)
    elif message.content.partition(' ')[0] == '!csgo':
        await play.csgo(message)
    elif message.content.partition(' ')[0] == '!uwu':
        response = (message.content+' ').split(' ', 1)[1]
        response = response.replace("r", "w")
        response = response.replace("l", "w")
        await message.channel.send(response)
    elif "bees" in message.content.lower():
        await bee_movie.bees(message)

    for content in thieyreChecker:
        if content.lower() in message.content:
            pick = random.randint(0,4)
            response = thieyreList[pick]
            await message.channel.send(response)



client.run(TOKEN)
