from bot_config import bot, dp
from aiogram.types import Message
import model
import view


@dp.message_handler(commands=['level'])
async def level_bot(message: Message):
    if not model.check_game():
        model.change_level()
        if model.get_bot_level() == 'Light':
            img = open('Nov.jpeg', 'rb')
            await bot.send_photo(message.chat.id, img)
            await view.level_light(message)
        else:
            img = open('Sup.jpeg', 'rb')
            await bot.send_photo(message.chat.id, img)
            await view.level_hard(message)
    else:
        await view.level_check(message)