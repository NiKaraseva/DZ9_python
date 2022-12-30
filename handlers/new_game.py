from bot_config import dp
from aiogram.types import Message
import model
import handlers


@dp.message_handler(commands=['new_game'])
async def start_new_game(message: Message):
    model.new_game()
    if model.check_game():
        await handlers.toss.toss_bot(message)
