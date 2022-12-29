from aiogram.types import Message
from bot_config import bot, dp
from aiogram.dispatcher.filters import Text

async def start_game(message: Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, '
                                                      f'приветствую тебя в игре Никины Конфетки! '
                                                      f'Вызвав команду /help, ты можешь ознакомиться с правилами игры.\n'
                                                      f'Если ты готов – выбирай уровень сложности, нажав команду /level.')


async def help_game(message: Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, '
                                                      f'рассказываю правила игры! Ты играешь против бота.\n'
                                                      f'Условия игры: на столе лежит 150 конфет, право первого хода определяется '
                                                      f'рандомом. За один ход можно забрать не более 28 конфет.\n'
                                                      f'Выигрывает тот, кто последний заберёт оставшиеся на столе конфеты.\n'
                                                      f'Если ты готов – нажимай /start. Да начнётся битва!')


async def toss_game(message: Message):
    await bot.send_message(message.from_user.id, text=f'Кидай жребий: напиши «орел» или «решка»')


async def toss_true(message: Message):
    await message.reply(text=f'{message.from_user.first_name}, да ты счастливчик! На столе сейчас 150 конфет.\n'
                            f'Ходи первым :)')


async def toss_false(message: Message):
    await message.reply(text=f'Хехе, первый ход за ботом.')



