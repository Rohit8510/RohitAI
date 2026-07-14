import os

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from services.openrouter import ask_image
from utils.helpers import split_message
from utils.logger import logger

TEMP_DIR = "temp"

os.makedirs(TEMP_DIR, exist_ok=True)


async def image_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )

    thinking = await update.message.reply_text(
        "🖼️ Image receive ho gayi...\n🤖 AI image analyze kar raha hai..."
    )

    file_path = None

    try:

        photo = update.message.photo[-1]

        telegram_file = await photo.get_file()

        file_path = os.path.join(
            TEMP_DIR,
            f"{user_id}.jpg"
        )

        await telegram_file.download_to_drive(file_path)

        answer = await ask_image(
            file_path,
            "Describe this image in detail. Reply in the same language as the user. Use emojis naturally."
        )

        try:
            await thinking.delete()
        except:
            pass

        parts = split_message(answer)

        for i, part in enumerate(parts):

            await update.message.reply_text(part)

        logger.info(
            f"[{user_id}] Image analyzed successfully."
        )

    except Exception as e:

        logger.exception(e)

        try:

            await thinking.edit_text(
                f"❌ Image Analysis Failed\n\n{e}"
            )

        except:
            pass

    finally:

        if file_path and os.path.exists(file_path):

            try:
                os.remove(file_path)
            except:
                pass
