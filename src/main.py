import discord
import os
import re

from summon import summon, SUMMON_CALL
from rh import rh, RH_CALL

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
rh_channel = client.get_channel(int(os.getenv("RH_BOT_RHCHID")))

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(RH_CALL):
        rh(client, message, rh_channel)
        return

    if message.content.startswith(SUMMON_CALL):
        summon(client, message)
        return


client.run(os.getenv("RH_BOT_DISCTOKEN"))
