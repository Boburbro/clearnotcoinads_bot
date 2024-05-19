from loader import bot
from telebot.types import Message
from telebot.util import content_type_media


@bot.message_handler(content_types=content_type_media)
async def command_start(message: Message):
    if "notcoin" in message.text.lower():
        await bot.delete_message(message.chat.id, message_id=message.message_id)
