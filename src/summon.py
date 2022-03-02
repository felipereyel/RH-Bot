from discord.channel import VoiceChannel

from utils import search_user

SUMMON_CALL = "sm"


async def summon(client, message):
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

    [reference, search] = search_user(SUMMON_CALL, message.content)

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
