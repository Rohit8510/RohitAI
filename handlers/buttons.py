from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from services.memory import clear_history, get_history, save_message
from services.openrouter import ask_ai
from services.cache import get_last_prompt, save_last

from utils.helpers import split_message
from utils.logger import logger


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

    user_id = query.from_user.id

    if query.data == "help":

        await query.message.reply_text(
            """🤖 RohitAI Help

/start - Start Bot
/help - Help
/newchat - New Chat
/clear - Clear Memory

😊 Bas message bhejo aur AI se baat karo.
"""
        )

    elif query.data == "clear":

        await clear_history(user_id)

        await query.message.reply_text(
            "✅ Chat Memory Cleared."
        )

    elif query.data == "newchat":

        await clear_history(user_id)

        await query.message.reply_text(
            "🆕 New Chat Started.\n😊 Hello!"
        )

    elif query.data == "regen":

        prompt = get_last_prompt(user_id)

        if not prompt:

            await query.message.reply_text(
                "⚠️ Pehle koi message bhejo."
            )
            return

        thinking = await query.message.reply_text(
            "🤖 Regenerating..."
        )

        try:

            history = await get_history(user_id)

            history.append(
                {
                    "role": "user",
                    "content": prompt
                }
            )

            answer = await ask_ai(history)

            save_last(
                user_id,
                prompt,
                answer
            )

            await save_message(
                user_id,
                "assistant",
                answer
            )

            try:
                await thinking.delete()
            except:
                pass

            parts = split_message(answer)

            for i, part in enumerate(parts):

                if i == len(parts) - 1:

                    await query.message.reply_text(
                        part,
                        reply_markup=reply_keyboard()
                    )

                else:

                    await query.message.reply_text(part)

            logger.info(
                f"[{user_id}] Regenerated Response"
            )

        except Exception as e:

            logger.exception(e)

            try:

                await thinking.edit_text(
                    "❌ Regenerate Failed."
                )

            except:

                await query.message.reply_text(
                    "❌ Regenerate Failed."
                )
