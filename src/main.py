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
        if cmd.match(message):
            await cmd.execute(client, message)
            return


client.run(os.getenv("RH_BOT_DISCTOKEN"))
