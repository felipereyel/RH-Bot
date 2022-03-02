import discord
import os

from summon import summon, SUMMON_CALL
from rh import rh, RH_CALL

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

    if message.content.startswith(RH_CALL):
        await rh(client, message)
        return

    if message.content.startswith(SUMMON_CALL):
        await summon(client, message)
        return


client.run(os.getenv("RH_BOT_DISCTOKEN"))
