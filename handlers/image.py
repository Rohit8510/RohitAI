from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes


async def image_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )

    try:

        photo = update.message.photo[-1]

        file = await photo.get_file()

        file_path = "temp_image.jpg"

        await file.download_to_drive(file_path)

        await update.message.reply_text(
            "📷 Image receive ho gayi.\n\n🤖 Ab AI image ko analyze karega..."
        )

        # Vision API Part 9.2 me add karenge

    except Exception as e:

        await update.message.reply_text(
            f"❌ Error:\n{e}"
        )
