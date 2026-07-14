from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from services.memory import (
    get_history,
    save_message,
)

from services.openrouter import ask_ai

from utils.helpers import split_message
from utils.logger import logger


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    user_message = update.message.text

    logger.info(f"{user_id}: {user_message}")

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING,
    )

    history = await get_history(user_id)

    history.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    answer = await ask_ai(history)

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

    for part in split_message(answer):
        await update.message.reply_text(part)