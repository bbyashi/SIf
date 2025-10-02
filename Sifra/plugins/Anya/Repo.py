from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Sifra import app as bot
import requests
from config import BOT_USERNAME
from Sifra.utils.errors import capture_err

start_txt = """**
⊚ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐌𝐘 𝐖𝐎𝐑𝐋𝐃 ⊚
 
➻ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ ʙʏ ᴜꜱɪɴɢ ᴛʜᴇꜱᴇ ʀᴇᴘᴏꜱ ✰
 
 ➻ ɴᴏ ᴇʀʀᴏʀ ✰
 
 ➻ ɴᴏ ʜᴇʀᴏᴋᴜ ᴀᴄᴄᴏᴜɴᴛ ʙᴀɴ ɪꜱꜱᴜᴇ ✰
 
➻ ɴᴏ ɪᴅ ʙᴀɴ ɪꜱꜱᴜᴇ✰
 
 ➻ ᴀʟʟ ʀᴇᴘᴏꜱ ᴡᴏʀᴋꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ʟᴀɢ ᴀꜰᴛᴇʀ ᴅᴇᴘʟᴏʏ ✰
 
 ► ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴅᴍ ᴀᴛ ꜱᴜᴘᴘᴏʀᴛ
**"""




@bot.on_message(filters.command(["repo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿", url="https://t.me/TEAM_X_T"),
          InlineKeyboardButton("𝙾𝚆𝙽𝙴𝚁", url="https://t.me/RAX_XT"),
          ],
               [
                InlineKeyboardButton("𝚆𝙰𝙽𝚃 𝙲𝙲", url=f"https://t.me/TEAM_X_T"),

],
[
              InlineKeyboardButton("𝙶𝙲 𝙳𝙴𝚂𝚃𝚁𝙾𝚈𝙴𝚁", url=f"https://github.com/subhichiku/BANALL"),
              InlineKeyboardButton("︎𝙼𝚄𝚂𝙸𝙲 𝙱𝙾𝚃", url=f"https://github.com/subhichiku/SUBHI"),
              ],
              [
              InlineKeyboardButton("𝙼𝙰𝙽𝙰𝙶𝙴𝙼𝙴𝙽𝚃 𝙱𝙾𝚃", url=f"https://github.com/subhichiku/CHIKU-ASSISTANT"),
InlineKeyboardButton("𝙲𝙷𝙰𝚃 𝙱𝙾𝚃", url=f"https://github.com/subhichiku/CHIKU-CHAT"),
],
[
InlineKeyboardButton("𝚂𝚃𝚁𝙸𝙽𝙶 𝙱𝙾𝚃", url=f"https://github.com/subhichiku/SUBHISTRING")
],
[
InlineKeyboardButton("𝚄𝚂𝙴𝚁 𝙱𝙾𝚃", url=f"https://github.com/subhichiku/USERBOT")
],

        ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/19832f573094d09e46762.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
