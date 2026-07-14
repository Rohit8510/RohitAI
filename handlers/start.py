from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🤖 *Welcome to RohitAI v2*

Main OpenRouter AI se powered Telegram Bot hoon.

Commands:

/start - Start Bot
/help - Help
/newchat - New Conversation
/clear - Clear Memory

Bas koi bhi message bhejo 😊
"""

    await update.message.reply_text(
        text,
        parse_mode="Markdown"
    )