#bee_movie.py

async def csgo(message):

    if message.content.split(' ', 2)[1].lower() == 'go':
        response = "Ok"
        await message.channel.send(response)
    elif message.content.split(' ', 2)[1].lower() == 'reload':
        response = "You have full ammo. Way to go"
        await message.channel.send(response)
    elif message.content.split(' ', 2)[1].lower() == 'shoot':
        response = "You missed. Noob"
        await message.channel.send(response)
    elif message.content.split(' ', 2)[1].lower() == 'camp':
        response = "You camper"
        await message.channel.send(response)
    else:
        response = "Please enter a valid command"
        await message.channel.send(response)
