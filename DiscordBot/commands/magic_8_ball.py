import random

async def ball(message):

    ### Easter eggs ###
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

    ### General responses ###
    else:
        responses = ['meh...', 'fuck if I know', 'no shit Sherlock', 'Is that a real question?', 'Survey Says: Fuck You', 'You know I think they teach that in like 3rd grade', 'In the words of Søren Aabye Kierkegaard, philosopher and father of existential humanism: Shut up and leave me alone', 'Absofuckinglutely', 'When hell freezes over', 'Idk I can\'t check right now, my wifi is out', 'Oh hell yeah', 'I mean I think so but I heard it from this guy who won\'t shut up about the moon landings so take that with a grain of salt', 'One sec I\'m taking a hit', 'Sure, one sec.\nHey Siri!\nSome dumbass wants to know ' + (message.content+' ').split(' ', 1)[1] + '\nApparently the answer is no', 'You\’re gonna want to take a seat for this one: No.', 'Sure… maybe. Maybe one day we’ll have peace on earth. Maybe Mitch McConnel will sing lead in a 70-plus NWA cover band. And yeah, maybe one day, your thing. What can I say? I’m an optimist.', 'No. And I don\’t just mean \"Sir, have you been drinking tonight?\" no. I mean, like, \"Do you think she still thinks about me?\" no.', 'Sometimes I hit the nail right on the head. Other times I\’m just hammered. Ask tomorrow.', 'Remember the words of the twenty-first century poet, Usher: \“Yeah.\”', 'Fuck yeah, bro. Don\’t even trip.', 'I gotchu.', 'Not while there’s a Dummycrat in the White House.', 'No. Honestly man, kinda fucked up that you would even ask that.', 'Dude, it’s late. Google that shit.', 'Do you seriously have to plan for everything? Jesus. Hakuna Matata.']
        await message.channel.send(responses[random.randint(0, len(responses) - 1)])
