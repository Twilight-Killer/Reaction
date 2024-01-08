from bot.config import Telegram

SupportedEmojisText = \
"""
**I currently support following emojis:**
""" + '\n'.join(' '.join(Telegram.EMOJIS[i:i+5]) for i in range(0, len(Telegram.EMOJIS), 5))
