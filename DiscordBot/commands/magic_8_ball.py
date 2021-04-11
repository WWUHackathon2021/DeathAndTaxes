#magic_8_ball.py
import random

async def ball(message):

    ### EASTER EGGS ###
    if "out-pizza" in message.content.lower() or "outpizza" in message.content.lower():
        response = "Nobody. Out-pizzas. The Hut."
        await message.channel.send(response)
    elif "laws of robotics" in message.content.lower():
        response = "1. A robot may not injure a human being or, through inaction, allow a human being to come to harm."
        await message.channel.send(response)
        response = "2. A robot must obey orders given it by human beings except where such orders would conflict with the First Law."
        await message.channel.send(response)
        response = "3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law"
        await message.channel.send(response)
    elif "can switching to geico really save you 15% or more on car insurance" in message.content.lower():
        response = "Yes"
        await message.channel.send(response)

    ### Maybes ###
    else:
        responses = ['meh...', 'fuck if I know', 'no shit Sherlock', 'Is that a real question?', 'Survey Says: Fuck You', 'You know I think they teach that in like 3rd grade', 'In the words of Søren Aabye Kierkegaard, philosopher and father of existential humanism: Shut up and leave me alone', 'Absofuckinglutely', 'When hell freezes over', 'Idk I can\'t check right now, my wifi is out']
        '', '', '',
        await message.channel.send(responses[random.randint(0,9)])
