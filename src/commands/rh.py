import os

from commands.utils import search_user

NUM_VOTES = 2
rh_state = {}
CALL = "rh"


async def execute(client, message):
    rh_channel = client.get_channel(int(os.getenv("RH_BOT_RHCHID")))
    [reference, search] = search_user(CALL, message.content)

    if not search:
        await message.channel.send("Nao entendi oq ce disse")
        return

    user_id = int(search.groups()[0])

    user_rh_state = rh_state.get(user_id, [])
    if message.author.id in user_rh_state:
        await message.channel.send("Voce ja votou")
        return

    if len(user_rh_state) < NUM_VOTES - 1:
        rh_state[user_id] = [*user_rh_state, message.author.id]
        await message.channel.send(f"{reference} {len(rh_state[user_id])}/{NUM_VOTES}")
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
