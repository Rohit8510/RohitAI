from telegram import Update
from telegram.ext import ContextTypes

from services.memory import clear_history


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await clear_history(update.effective_user.id)

    await update.message.reply_text(
        "✅ Memory Cleared."
    )


async def newchat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await clear_history(update.effective_user.id)

    await update.message.reply_text(
        "🆕 New Chat Started."
    )