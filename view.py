from aiogram.types import Message
from bot_config import bot
import model


async def start_game(message: Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, '
                                                      f'приветствую тебя в игре Никины Конфетки! '
                                                      f'С помощью команды /help на клавиатуре ты можешь ознакомиться с правилами игры.\n'
                                                      f'С помощью команды /level на клавиатуре ты можешь выбрать уровень игры.\n'
                                                      f'Для начала игры нажми /new_game.')


async def help_game(message: Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, '
                                                      f'рассказываю правила игры! Ты играешь против бота.\n'
                                                      f'Условия игры: на столе лежит 150 конфет, право первого хода определяется '
                                                      f'рандомом. За один ход можно забрать не более 28 конфет.\n'
                                                      f'Выигрывает тот, кто последний заберёт оставшиеся на столе конфеты.\n'
                                                      f'Если ты готов – нажимай /start. Да начнётся битва!')


async def toss_game(message: Message):
    await bot.send_message(message.from_user.id, text=f'Кидай жребий: напиши «Орел» или «Решка»')


async def toss_true(message: Message, draw_text):
    await message.reply(text=f'Результат жеребьёвки: {draw_text}. {message.from_user.first_name}, да ты счастливчик! На столе сейчас 150 конфет.\n'
                            f'Ходи первым :)')


async def toss_false(message: Message, draw_text):
    await message.reply(text=f'Результат жеребьёвки: {draw_text}. Хехе, первый ход за ботом.')


async def take_zero(message: Message):
    await message.reply(text=f'Можно взять только положительное количество конфет. Попробуй-ка ещё раз!')

async def take_over(message: Message):
    await message.reply(text=f'Возьми-ка поменьше конфет!')

async def take_digit(message: Message):
    await message.reply(text=f'Эй, нужно ввести число!')

async def take_more_total(message: Message):
    await message.reply(text=f'Ты хочешь взять больше конфет, чем осталось. Будь внимательнее, ты почти победил ;)')

async def take_game(message: Message):
    await message.answer(text=f'{message.from_user.first_name} взял со стола {message.text} конфет. На столе осталось {model.get_total()} конфет.')


async def bot_game(message, take_bot):
    await message.answer(text=f'Бот взял со стола {take_bot} конфет. На столе осталось {model.get_total()} конфет.')


async def player_turn_message(message: Message):
    await message.answer(text=f'Твоя очередь, человек!')

async def player_win(message: Message):
    await message.answer(text=f'Да ты конфетный супермен! Поздравляю с выигрышем!')

async def bot_win(message: Message):
    await message.answer(text=f'Эх, а бот оказался умнее тебя :( Бот победил!')


async def level_light(message: Message):
    await message.answer(text=f'Уровень сложности – новичок. Самое время поиграться в конфетки!\n'
                              f'Набери /new_game для начала игры.')

async def level_hard(message: Message):
    await message.answer(text=f'Уровень сложности – конфетный супермен. Посмотрим, удастся ли тебе перехитрить искусственный интеллект!\n'
                              f'Набери /new_game для начала игры.')

async def level_check(message: Message):
    await message.answer(text=f'Данную настройку можно изменить только после окончания партии.')