import discord
import asyncio

import bot.config as config
import bot.message_util as message_util

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {} #{}'.format(client.user.name, client.user.id))

@client.event
async def on_message(message):
    for word in config.BANNED_WORDS:
        if message_util.contains_pattern(message.content.lower(), word):
            await client.send_message(message.channel, config.BANNED_MESSAGE)
            break

def start():
    client.run(config.BOT_TOKEN)
