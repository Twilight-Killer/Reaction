from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import TelegramBot
from bot.config import Telegram
from bot.modules.static import *

@TelegramBot.on_message(
    filters.command('emojis')
    & (
        filters.private |
        filters.group
    )
)
async def send_emojis(_, msg: Message):
    return await msg.reply(
        text=SupportedEmojisText,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='Reference', url='t.me/DarkiezZzz')
                ]
            ]
        )
    )
