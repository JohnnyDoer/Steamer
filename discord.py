#!/usr/bin/python3
# Imports from modules.
import discord
import asyncio
import time

from steam import BOT_TOKEN


# Discord Bot.
client = discord.Client()


# Runs on start of the script.
@client.event
async def on_ready():
    print('Logged in as:', client.user.name, client.user.id)
    print('---------------------------------------')
    print('Bot started.\n\n\n')


# Runs whenever a message is received on discord.
@client.event
async def on_message(message):

    # To save all server text channels in channels.txt.
    getChannel(message)

    # To save all server members channels in members.txt.
    getMember(message)

    # Don't do anything when this Bot sends messages.
    if message.author == client.user:
        return

    # To add items to the wishlist.
    if message.content.startswith("!wish"):
        if message.channel.name != "makeawish":
            return
        for i in addWish(message):
            await message.channel.send(i)
        await asyncio.sleep(100)

    # To remove items from the wishlist.
    if message.content.startswith("!remove"):
        pass

    # To start the market checker.
    if message.content.startswith("!start"):
        while True:
            for i in steamPrice():
                await message.channel.send(i)
            await asyncio.sleep(100)


# Run the Bot.
client.run(BOT_TOKEN)
