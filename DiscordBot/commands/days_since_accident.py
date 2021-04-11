#days_since_accident.py
import random
import datetime

trackedMessages = []
trackedTimes = []

async def accident(message):

    ### Check for content ###
    now = datetime.datetime.now()

    content = message.content.replace("!track ", "")
    content = content.replace("!reset ", "")
    content = content.replace("!check ", "")
    
    if message.content.partition(' ')[0] == '!track':
        trackedMessages.append(content)
        trackedTimes.append(now)
        await message.channel.send("Tracking time since " + content + ". Feh. good luck with that shit, we know how this goes. *rolls eyes*.")

    pos = trackedMessages.index(content)
    time_delta = (now - trackedTimes[pos])
    change_seconds = time_delta.total_seconds()/1
    change_minutes = change_seconds/60
    change_hours = change_minutes/60
    change_days = change_hours/24
    time_string = str(change_days) + " days, " + str(change_hours) + " hours, " + str(change_minutes) + " minutes, " + str(change_seconds) + " seconds."

    if message.content.partition(' ')[0] == '!reset':
        pos = trackedMessages.index(content)
        await message.channel.send("Wow, its only been " + time_string + " since " + content + ". Way to 'break' the cycle =_=. Everyone was REALLLLY expecting this to succeed *spits in your direction*.")
        trackedTimes[pos] = now

    if message.content.partition(' ')[0] == '!check':
        pos = trackedMessages.index(content)
        await message.channel.send("It has been " + time_string + " since " + content + ". Wow, you'd think this would have been reset by now, huh.")