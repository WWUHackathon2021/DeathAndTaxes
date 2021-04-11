#days_since_accident.py
import random

async def accident(message):

    ### Check for content ###

    if message.content.partition(' ')[0] == '!track':
        message.channel.send("not implemented")
    if message.content.partition(' ')[0] == '!reset':
        message.channel.send("not implemented")
    if message.content.partition(' ')[0] == '!check':
        message.channel.send("not implemented")