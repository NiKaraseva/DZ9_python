import random
from aiogram.dispatcher.filters import Text
from bot_config import dp
from aiogram.types import Message
import view
import handlers


@dp.message_handler(Text(equals=('орел', 'решка')))
async def lottery_bot(message: Message):
    draw = random.shuffle('орел', 'решка')
    if message.text == draw:
        await view.toss_true(message)
    else:
        await view.toss_false(message)
        await handlers.bot_turn(message)

