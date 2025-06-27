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

# Load config variables
if exists("config.py"):
    from config import *
else:
    from sample_config import *

# Database connection
conn = connect(DB_NAME)

# Define variables to be initialized later
spr = None
arq = None
BOT_USERNAME = None
BOT_ID = None
session = None


async def initialize():
    global spr, arq, BOT_ID, BOT_USERNAME, session

    session = ClientSession()
    arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)

    spr = Client(
        SESSION_NAME,
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
    )

    await spr.start()
    bot = await spr.get_me()
    BOT_ID = bot.id
    BOT_USERNAME = bot.username

    print(f"✅ Bot started as @{BOT_USERNAME} [ID: {BOT_ID}]")


# Expose important objects
__all__ = ["spr", "arq", "BOT_USERNAME", "BOT_ID", "conn", "session"]
