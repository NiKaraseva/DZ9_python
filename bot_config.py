import os
from aiogram import Bot, Dispatcher



bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher(bot)
