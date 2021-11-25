import discord
import os
import re

from discord.channel import VoiceChannel

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

NUM_VOTES = 2
RH_CALL = "rh"
SUMMON_CALL = "sm"
rh_state = {}


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    rh_channel = client.get_channel(os.getenv("RH_ID"))

    if message.content.startswith(RH_CALL):
        reference = message.content.replace(RH_CALL, "").strip()
        search = re.search(r"<@!(\d*)>", reference)

        if not search:
            await message.channel.send("Nao entendi oq ce disse")
            return

        user_id = int(search.groups()[0])

        user_rh_state = rh_state.get(user_id, [])
        if len(user_rh_state) < NUM_VOTES - 1:
            rh_state[user_id] = [*user_rh_state, message.author.id]
            await message.channel.send(
                f"{reference} {len(rh_state[user_id])}/{NUM_VOTES}"
            )
        else:
            for member in client.get_all_members():
                if member.id == user_id:
                    try:
                        await member.move_to(rh_channel)
                        await message.channel.send(
                            f"{reference} movido pro RH por comportamento ruim"
                        )
                    except Exception:
                        print("deu xabu")
                    rh_state.pop(user_id)
                    break
            else:
                await message.channel.send("Nao achei o usuario")
        return

    if message.content.startswith(SUMMON_CALL):
        ref_channel = None
        for channel in client.get_all_channels():
            if not isinstance(channel, VoiceChannel):
                continue
            if message.author.id in [m.id for m in channel.members]:
                ref_channel = client.get_channel(channel.id)
                break

        if not ref_channel:
            await message.channel.send("voce nao esta conectado")
            return

        reference = message.content.replace(SUMMON_CALL, "").strip()
        search = re.search(r"<@!(\d*)>", reference)

        if not search:
            await message.channel.send("Nao entendi oq ce disse")
            return

        user_id = int(search.groups()[0])
        for member in client.get_all_members():
            if member.id == user_id:
                try:
                    await member.move_to(ref_channel)
                except Exception:
                    print("deu xabu")
                break
        else:
            await message.channel.send("Nao achei o usuario")


client.run(os.getenv("TOKEN"))
