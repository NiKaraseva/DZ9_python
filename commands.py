from bot_config import bot, dp
from aiogram import types
from random import randint as rnd


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, '
                                                      f'приветствую тебя в игре Ника и Конфетки! '
                                                      f'Вызвав команду /help ты можешь ознакомиться с правилами игры.\n'
                                                      f'Если готов – бросай кубик (нажми 0 или 1).')



@dp.message_handler(commands=['help'])
async def help_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, '
                                                      f'рассказываю правила игры! Ты играешь против бота.\n'
                                                      f'Условия игры: на столе лежит 150 конфет, право первого хода определяется '
                                                      f'рандомом. За один ход можно забрать не более 28 конфет.\n'
                                                      f'Выигрывает тот, кто последний заберёт оставшиеся на столе конфеты.\n'
                                                      f'Если ты готов – нажимай /start. Да начнётся битва!')

total_sweets = 150
turn = 0


@dp.message_handler()
async def first_move(message: types.Message):
    global turn
    if message.text.isdigit():
        if int(message.text) != 0 and int(message.text) != 1:
            await message.reply(f'Введи 0 или 1.')
        else:
            draw = rnd(0, 1)
            if int(message.text) == draw:
                await message.reply(f'Жребий равен {draw}. {message.from_user.first_name}, да ты счастливчик! Ходи первым :)')
                turn = 1
            else:
                await message.reply(f'Жребий равен {draw}. Хехе, первый ход за ботом.')
                turn = 2
    else:
        await message.reply(f'Введи цифру 0 или 1 (а не слово)!')



@dp.message_handler()
async def player_turn(message: types.Message):
    global total_sweets
    global turn
    if turn == 1:
        if total_sweets > 0:
            if message.text.isdigit():
                total_sweets -= int(message.text)
                if 0 < int(message.text) < 29:
                    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name} взял со стола '
                                                                      f'{message.text} конфет.\n'
                                                                      f'На столе осталось {total_sweets} кофет.\n'
                                                                      f'Очередь бота.')
                else:
                    await message.reply(f'Возьми-ка поменьше конфет!')
            else:
                await message.reply(f'Эй, нужно ввести число!')
        else:
            await message.reply(f'Эх, а бот оказался умнее тебя :( Бот победил!\n'
                                f'Сыграем заново? Жми /start!')











# total_sweets = 150
# player_sweets = 0
# bot_sweets = 0
# take_sweets = 0
#
#
# def FirstMove():
#     draw = rnd(0, 1)
#     print(f'Жребий = {draw}')
#     if draw == 0:
#         PlayerTurn()
#     else:
#         BotTurn()
#
#
# def PlayerTurn():
#     global take_sweets
#     global total_sweets
#     global player_sweets
#     take_sweets = int(input(f'На столе сейчас {total_sweets}. Сколько конфет вы хотите взять? '))
#     while take_sweets > total_sweets or take_sweets > 28 or take_sweets <= 0:
#         take_sweets = int(input('Вы играете не по правилам! Возьмите количество конфет от 1 до 28: '))
#     total_sweets -= take_sweets
#     player_sweets += take_sweets
#     if total_sweets > 0:
#         BotTurn()
#     else:
#         print('Поздравляю! Вы победили!')
#
#
# def BotTurn():
#     global take_sweets
#     global total_sweets
#     global bot_sweets
#     if total_sweets % 29 != 0:
#         take_sweets = total_sweets % 29
#     else:
#         take_sweets = rnd(1, 28)
#     total_sweets -= take_sweets
#     bot_sweets += take_sweets
#     print(f'Бот взял {take_sweets} конфет.')
#     if total_sweets > 0:
#         PlayerTurn()
#     else:
#         print('Бот красавчик!')
#
# FirstMove()