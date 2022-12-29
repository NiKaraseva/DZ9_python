import random
from bot_config import bot
from aiogram.types import Message
from random import randint as rnd
import view


async def bot_turn(message: Message):
    global total_sweets
    global player
    # if player == 'Nov':
    #     take_sweets_bot = rnd(1, 28)
    # else:
    take_sweets_bot = total_sweets % 29 if total_sweets % 29 != 0 else rnd(1, 28)
    total_sweets -= take_sweets_bot
    await bot.send_message(message.from_user.id, text=f'Бот взял со стола {take_sweets_bot} конфет. На столе осталось {total_sweets} конфет.')
    if total_sweets > 0:
        await bot.send_message(message.from_user.id, text=f'Твоя очередь, человек!')
    else:
        await bot.send_message(message.from_user.id, text=f'Эх, а бот оказался умнее тебя :( Бот победил!')
        total_sweets = 150
        await bot.send_message(message.from_user.id, text=f'Сыграем заново?) Жмакай /start!')