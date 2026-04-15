import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AnsikaMusic import LOGGER, app, userbot
from AnsikaMusic.core.call import SHUKLA
from AnsikaMusic.misc import sudo
from AnsikaMusic.plugins import ALL_MODULES
from AnsikaMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("ᴋʏ ᴄʜᴇʀᴀ ʙᴏsᴅɪ")
        
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AnsikaMusic.plugins" + all_module)
    LOGGER("AnsikaMusic.plugins").info("ᴋʏ ᴄʜᴇʀᴀ ʙᴏsᴅɪ...")
    await userbot.start()
    await SHUKLA.start()
    await SHUKLA.decorators()
    LOGGER("AnsikaMusic").info(
        "ᴋʏ ᴄʜᴇʀᴀ ʙᴏsᴅɪ"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AnsikaMusic").info("ᴋʏ ᴄʜᴇʀᴀ ʙᴏsᴅɪ")
    

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
