from bot_config import dp
from aiogram.types import Message
import view

@dp.message_handler(commands=['help'])
async def help_bot(message: Message):
   await view.help_game(message)

