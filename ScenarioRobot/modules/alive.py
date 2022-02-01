import re

import os

from telethon import events, Button

from telethon import __version__ as tlhver

from pyrogram import __version__ as pyrover

from ScenarioRobot.events import register as MEMEK

from ScenarioRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/50c21b237d00309571e00.jpg"

@MEMEK(pattern=("/alive"))

async def awake(event):

  tai = event.sender.first_name

  SCENARIO = "**Hello I'm Scenario!** \n\n"

  SCENARIO += "🔥 **I'm Working Properly** \n\n"

  SCENARIO += "🔥 **My Master : [Akku](https://t.me/userderdead)** \n\n"

  SCENARIO += f"🔥 **Telethon Version : {tlhver}** \n\n"

  SCENARIO += f"🔥 **Pyrogram Version : {pyrover}** \n\n"

  SCENARIO += "**Thanks For Adding Me Here ❤️**"

  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Golden_gang_bot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/noobxsupport")]]

  await tbot.send_file(event.chat_id, PHOTO, caption=SCENARIO,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))

async def reload(event):

  tai = event.sender.first_name

  SCENARIO = "✅ **scenario restarted successfully**\n\n• Admin list has been **updated**"

  BUTTON = [[Button.url(" ᴜᴘᴅᴀᴛᴇs", "https://t.me/noobxupdates")]]

  await tbot.send_file(event.chat_id, PHOTO, caption=SCENARIO,  buttons=BUTTON)
