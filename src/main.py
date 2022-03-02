import discord
import os
from commands import commands

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for cmd in commands:
        if message.content.startswith(cmd.CALL):
            await cmd.execute(client, message)
            break


client.run(os.getenv("RH_BOT_DISCTOKEN"))
