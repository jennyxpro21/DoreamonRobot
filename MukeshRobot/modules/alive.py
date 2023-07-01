import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID,BOT_NAME,START_IMG

PHOTO = [
    "https://telegra.ph/file/d2a23fbe48129a7957887.jpg",
    "https://telegra.ph/file/ddf30888de58d77911ee1.jpg",
    "https://telegra.ph/file/268d66cad42dc92ec65ca.jpg",
    "https://telegra.ph/file/13a0cbbff8f429e2c59ee.jpg",
    "https://telegra.ph/file/bdfd86195221e979e6b20.jpg",
]

Mukesh = [
    [
        InlineKeyboardButton(text="💓𝐎ɯɳҽ𝐑💓", user_id=OWNER_ID),
        InlineKeyboardButton(text="💓𝐒υρρσɾ𝐓💓", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="➕𝐀ԃ𝐃 𝐌ҽ 𝐓σ 𝐘συ𝐑 𝐆ɾσυ𝐏➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]



@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.2)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.1)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")

    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await m.reply_sticker(
        "CAACAgEAAxkBAANNZKBV19JCLCmNMqZKS-BO2X-pR-kAAssCAAKZmnhEQtw4iGsO8FUvBA"
    )
    await umm.delete()
    await asyncio.sleep(0.2)
    await m.reply_photo(
        START_IMG,
        caption=f"""**𝐇ҽ𝐘, 𝐈 𝐀ɱ 『[{BOT_NAME}](f"t.me/{BOT_USERNAME}")』**
   ━━━━━━━━━━━━━━━━━━━
  » **𝐌ყ 𝐎ɯɳҽ𝐑 :** [𝐎ɯɳҽ𝐑](tg://user?id={OWNER_ID})
  
  » **𝐋ιႦɾαɾ𝐘 𝐕ҽɾʂισ𝐍 :** `{lver}`
  
  » **𝐓ҽʅҽƚԋσ𝐍 𝐕ҽɾʂισ𝐍 :** `{tver}`
  
  » **𝐏ყɾσɠɾα𝐌 𝐕ҽɾʂισ𝐍 :** `{pver}`
  
  » **𝐏ყƚԋσ𝐍 𝐕ҽɾʂισ𝐍 :** `{pyver()}`
   ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(Mukesh),
    )
