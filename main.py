from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

import config
from database import init_database

from handlers.start import start
from handlers.help import help_command
from handlers.chat import chat
from handlers.admin import clear, newchat
from handlers.buttons import button_click

from utils.logger import logger


async def post_init(application: Application):
    await init_database()
    logger.info("✅ Database Initialized")
    logger.info("🤖 RohitAI Started")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.exception(
        "Unhandled Exception",
        exc_info=context.error
    )


def main():

    if not config.BOT_TOKEN:
        raise ValueError("BOT_TOKEN missing in .env")

    if not config.OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY missing in .env")

    app = (
        Application.builder()
        .token(config.BOT_TOKEN)
        .build()
    )

    app.post_init = post_init

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(CommandHandler("newchat", newchat))

    # Chat Messages
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            chat
        )
    )

    # Inline Buttons
    app.add_handler(
        CallbackQueryHandler(button_click)
    )

    # Error Handler
    app.add_error_handler(error_handler)

    logger.info("🚀 Polling Started...")

    app.run_polling(
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()
