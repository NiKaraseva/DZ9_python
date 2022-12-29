from bot_config import dp
from aiogram.types import Message
import view


@dp.message_handler(commands=['toss'])
async def toss_bot(message: Message):
    await view.toss_game(message)