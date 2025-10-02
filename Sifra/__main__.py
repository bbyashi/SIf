import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Sifra import LOGGER, app, userbot
from Sifra.core.call import Ayano
from Sifra.misc import sudo
from Sifra.plugins import ALL_MODULES
from Sifra.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    # Check assistant string sessions
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()

    # Load sudo users
    await sudo()

    # Load banned users from DB
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER("Sifra").warning(f"Error while loading banned users: {e}")

    # Start main bot
    await app.start()

    # Load all plugins
    loaded = []
    failed = []
    skipped = []

    for all_module in ALL_MODULES:
        module = all_module.strip().replace("\\", ".").replace("/", ".")
        if not module:
            skipped.append(all_module)
            continue
        try:
            importlib.import_module(f"Sifra.plugins.{module}")
            loaded.append(module)
        except ModuleNotFoundError:
            skipped.append(module)
            LOGGER("Sifra.plugins").warning(f"⚠️ Plugin not found: {module}")
        except Exception as e:
            failed.append(module)
            LOGGER("Sifra.plugins").error(f"❌ Failed to import {module}: {e}")

    # Summary of plugin imports
    if loaded:
        LOGGER("Sifra.plugins").info(f"✅ Loaded plugins: {', '.join(loaded)}")
    if skipped:
        LOGGER("Sifra.plugins").warning(f"⚠️ Skipped plugins: {', '.join(skipped)}")
    if failed:
        LOGGER("Sifra.plugins").error(f"❌ Failed plugins: {', '.join(failed)}")

    # Start userbot + call handler
    await userbot.start()
    await Ayano.start()

    try:
        await Ayano.stream_call("https://telegra.ph/file/f59799c8d94c4691939a4.mp4")
    except NoActiveGroupCall:
        LOGGER("Sifra").error("ᴠᴄ ᴛᴏ ᴏɴ ᴋʀ ʟᴇ ᴘᴇʜʟᴇ ғɪʀ ᴅᴇᴘʟᴏʏ ᴋʀ...")
        exit()
    except Exception:
        pass

    # Decorators setup
    await Ayano.decorators()

    # Final status
    LOGGER("Sifra").info(
        "ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ, ᴀᴀʙ ᴄʜᴀɴɴᴇʟ Jᴏɪɴ ᴋʀ ʟᴇ @PAHADI_VERSE"
    )

    # Idle until stopped
    await idle()

    # Cleanup on exit
    await app.stop()
    await userbot.stop()
    LOGGER("Sifra").info("ᴍᴀᴀ ᴄʜᴜᴅᴀ ᴍᴀɪɴ ʙᴏᴛ ʙᴀɴᴅ ᴋᴀʀ ʀʜᴀ Sifra Mᴜsɪᴄ Bᴏᴛ...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
