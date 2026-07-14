from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from services.memory import clear_history


def reply_keyboard():

    keyboard = [
        [
            InlineKeyboardButton(
                "🔄 Regenerate",
                callback_data="regen"
            ),
            InlineKeyboardButton(
                "🆕 New Chat",
                callback_data="newchat"
            )
        ],
        [
            InlineKeyboardButton(
                "🗑️ Clear",
                callback_data="clear"
            ),
            InlineKeyboardButton(
                "ℹ️ Help",
                callback_data="help"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


async def button_click(update: Update,
                       context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "help":

        await query.message.reply_text(
            """
🤖 RohitAI Help

/start
/help
/newchat
/clear

Bas message bhejo 😊
"""
        )

    elif query.data == "clear":

        await clear_history(
            query.from_user.id
        )

        await query.message.reply_text(
            "✅ Chat Memory Cleared"
        )

    elif query.data == "newchat":

        await clear_history(
            query.from_user.id
        )

        await query.message.reply_text(
            "🆕 New Chat Started"
        )

    elif query.data == "regen":

        await query.message.reply_text(
            "⚠️ Regenerate feature Part 8 me add karenge 😊"
        )
