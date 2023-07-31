from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config

xotic = "https://te.legra.ph/file/0387fbf52c52b7072407f.jpg"
def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴩ & Cᴏᴍᴍᴀɴᴅs",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="Sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴩ & Cᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text=" Sᴜᴩᴩᴏʀᴛ ", url="t.me/RadhaX2Support"
            ),
            InlineKeyboardButton(
                text=" Sᴛᴀᴛᴜs ", url="t.me/RadhaX2Update"
            )
        ],
        [
            InlineKeyboardButton(
                text=" Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ", url=xotic
            ),
            InlineKeyboardButton(
                text=" Oᴡɴᴇʀ ", url="t.me/MissRadha"
            )
        ],
     ]
    return buttons
