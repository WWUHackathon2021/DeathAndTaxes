
global uwumode

def init():
    global uwumode
    uwumode = False

async def uwuCommand(message):
    response = (message.content+' ').split(' ', 1)[1]
    response = uwu(response)
    await message.channel.send(response)

async def toggleUwuMode(message, print):
    global uwumode
    if uwumode:
        uwumode = False
        if print:
            response = "uwu mode deactivated"
            await respond(message, response)
    else:
        uwumode = True
        if print:
            response = "uwu mode activated"
            await respond(message, response)

def uwu(string):
    string = string.replace("r", "w")
    string = string.replace("l", "w")
    string = string.replace("R", "W")
    string = string.replace("L", "W")
    return string

async def respond(message, response):
    global uwumode
    if uwumode:
        response = uwu(response)
        await message.channel.send(response)
    else:
        await message.channel.send(response)
