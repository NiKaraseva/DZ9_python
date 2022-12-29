import random
from aiogram.dispatcher.filters import Text
import bot_turn
from bot_config import dp
from aiogram.types import Message
import view


@dp.message_handler(Text(equals=('Орел', 'Решка')))
async def lottery_bot(message: Message):
    draw_list = ['Орел', 'Решка']
    draw = random.choice(draw_list)
    if message.text == draw:
        await view.toss_true(message, draw)
    else:
        await view.toss_false(message, draw)
        await bot_turn.bot_turn(message)

