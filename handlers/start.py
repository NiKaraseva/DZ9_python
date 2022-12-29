import handlers
from bot_config import bot, dp
from aiogram.types import Message
import view


@dp.message_handler(commands=['start'])
async def start_bot(message: Message):
    img = open('konfetki.jpeg', 'rb')
    await bot.send_photo(message.chat.id, img)
    await view.start_game(message)
    await handlers.toss(message)
