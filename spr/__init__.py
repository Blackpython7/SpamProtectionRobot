from os.path import exists
from sqlite3 import connect

from aiohttp import ClientSession
from pyrogram import Client
from Python_ARQ import ARQ
import asyncio

SESSION_NAME = "spr"
DB_NAME = "db.sqlite3"
API_ID = 6
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
ARQ_API_URL = "https://arq.hamker.dev"

if exists("config.py"):
    from config import *
else:
    from sample_config import *

conn = connect(DB_NAME)

async def main():
    async with ClientSession() as session:
        arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)

        async with Client(
            SESSION_NAME,
            bot_token=BOT_TOKEN,
            api_id=API_ID,
            api_hash=API_HASH,
        ) as spr:
            bot = await spr.get_me()
            BOT_ID = bot.id
            BOT_USERNAME = bot.username

            print(f"Bot started: @{BOT_USERNAME} (ID: {BOT_ID})")
            # yahan se further logic call karo (handlers, loops, etc.)
            await asyncio.Event().wait()  # keep bot running

if __name__ == "__main__":
    asyncio.run(main())
