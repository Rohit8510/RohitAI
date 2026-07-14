from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
📖 Help

Available Commands

/start

/help

/newchat

/clear

Bas message bhejo aur AI reply karega.
"""

    await update.message.reply_text(text)