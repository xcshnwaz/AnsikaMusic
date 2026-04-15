from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from SHUKLAMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("donate")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://litter.catbox.moe/ad87gha5nzsputs1.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐃ᴏɴᴀᴛᴇ", url=f"https://t.me/cylxu")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("donate")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://litter.catbox.moe/ad87gha5nzsputs1.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐃ᴏɴᴀᴛᴇ", url=f"https://t.me/cylxu")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("donate")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://litter.catbox.moe/ad87gha5nzsputs1.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐃𝐨𝐧𝐚𝐭𝐞 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐃ᴏɴᴀᴛᴇ", url=f"https://t.me/cylxu")
                ]
            ]
        ),
    )
