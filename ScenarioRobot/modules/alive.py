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

  SCENARIO += "ð¥ **Master I'm Working Properly** \n\n"

  SCENARIO += "ð¥ **My Master : [Akku](https://t.me/userderdead)** \n\n"

  SCENARIO += f"ð¥ **Python :** __3.9.7__ ** \n\n"

  SCENARIO  += f"ð¥ **Pyrogram :** __1.2.9__ ** \n\n"

  SCENARIO += f"ð¥ **Telethon Version : {tlhver}** \n\n"

  SCENARIO += f"ð¥ **Pyrogram Version : {pyrover}** \n\n"

  SCENARIO += "**Thanks For Adding Me Here â¤ï¸**"

  BUTTON = [[Button.url("Êá´Êá´", "https://t.me/Golden_gang_bot?start=help"), Button.url("sá´á´á´á´Êá´", "https://t.me/noobxsupport")]]

  await tbot.send_file(event.chat_id, PHOTO, caption=SCENARIO,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))

async def reload(event):

  tai = event.sender.first_name

  SCENARIO = "â **Scenario reloaded successfully**\n\nâ¢ Admin list has been **updated**"

  BUTTON = [[Button.url(" á´á´á´á´á´á´s", "https://t.me/TeamScenario")]]

  await tbot.send_file(event.chat_id, PHOTO, caption=SCENARIO,  buttons=BUTTON)
