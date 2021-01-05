#!/usr/bin/python3
# Imports from modules.
import discord
import asyncio
import time

from steam import BOT_TOKEN


client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as:', client.user.name, client.user.id)
    print('---------------------------------------')
    print('Bot started.\n\n\n')


@client.event
async def on_message(message):

    getChannel(message)
    getMember(message)

    if message.author == client.user:
        return

    if message.content.startswith("!wish"):
        if message.channel.name != "makeawish":
            return
        for i in addWish(message):
            await message.channel.send(i)
        await asyncio.sleep(100)

    if message.content.startswith("!remove"):
        pass

    if message.content.startswith("!start"):
        while True:
            for i in steamPrice():
                await message.channel.send(i)
            await asyncio.sleep(100)


client.run(BOT_TOKEN)
