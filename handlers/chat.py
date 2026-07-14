from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from handlers.buttons import reply_keyboard

from services.memory import (
    get_history,
    save_message,
)

from services.openrouter import ask_ai
from services.cache import save_last

from utils.helpers import split_message
from utils.logger import logger


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    user_message = update.message.text

    logger.info(f"[{user_id}] User: {user_message}")

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )

    thinking = await update.message.reply_text(
        "🤖 Thinking..."
    )

    try:

        history = await get_history(user_id)

        history.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        answer = await ask_ai(history)

        # Save last prompt for regenerate
        save_last(
            user_id,
            user_message,
            answer
        )

        # Save in SQLite
        await save_message(
            user_id,
            "user",
            user_message
        )

        await save_message(
            user_id,
            "assistant",
            answer
        )

        try:
            await thinking.delete()
        except Exception:
            pass

        parts = split_message(answer)

        for i, part in enumerate(parts):

            if i == len(parts) - 1:

                await update.message.reply_text(
                    part,
                    reply_markup=reply_keyboard()
                )

            else:

                await update.message.reply_text(
                    part
                )

        logger.info(
            f"[{user_id}] Reply Sent"
        )

    except Exception as e:

        logger.exception(e)

        try:

            await thinking.edit_text(
                "❌ Sorry, kuch problem aa gayi.\n\nPlease thodi der baad try karo. 😊"
            )

        except Exception:
            pass
