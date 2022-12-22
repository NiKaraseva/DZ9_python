from bot_config import bot, dp
from aiogram import types
from random import randint as rnd


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    img = open('konfetki.jpeg', 'rb')
    await bot.send_photo(message.chat.id, img)
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, '
                                                      f'приветствую тебя в игре Ника и Конфетки! '
                                                      f'Вызвав команду /help ты можешь ознакомиться с правилами игры.\n'
                                                      f'Если ты готов – нажми команду \n'
                                                      f'/lottery, чтобы кинуть жребий.')



@dp.message_handler(commands=['help'])
async def help_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, '
                                                      f'рассказываю правила игры! Ты играешь против бота.\n'
                                                      f'Условия игры: на столе лежит 150 конфет, право первого хода определяется '
                                                      f'рандомом. За один ход можно забрать не более 28 конфет.\n'
                                                      f'Выигрывает тот, кто последний заберёт оставшиеся на столе конфеты.\n'
                                                      f'Если ты готов – нажимай /start. Да начнётся битва!')


@dp.message_handler(commands=['lottery'])
async def first_move(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'Кидай жребий: набери 100 или 101')


@dp.message_handler(text='100' or '101')
async def lottery(message: types.Message):
    draw = rnd(100, 101)
    if int(message.text) == draw:
        await message.reply(f'Жребий равен {draw}. {message.from_user.first_name}, да ты счастливчик! На столе сейчас 150 конфет.\n'
                            f'Ходи первым :)')
    else:
        await message.reply(f'Жребий равен {draw}. Хехе, первый ход за ботом.')
        await bot_turn(message)


total_sweets = 150

async def bot_turn(message: types.Message):
    global total_sweets
    take_sweets_bot = total_sweets % 29 if total_sweets % 29 != 0 else rnd(1, 28)
    total_sweets -= take_sweets_bot
    await bot.send_message(message.from_user.id, text=f'Бот взял со стола {take_sweets_bot} конфет. На столе осталось {total_sweets} конфет.')
    if total_sweets > 0:
        await bot.send_message(message.from_user.id, text=f'Твоя очередь, человек!')
    else:
        await bot.send_message(message.from_user.id, text=f'Эх, а бот оказался умнее тебя :( Бот победил!')
        total_sweets = 150
        await bot.send_message(message.from_user.id, text=f'Сыграем заново?) Жмакай /start!')


@dp.message_handler()
async def player_turn(message: types.Message):
    global total_sweets
    if message.text.isdigit():
        if 0 < int(message.text) < 29:
            total_sweets -= int(message.text)
            await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name} взял со стола '
                                                              f'{message.text} конфет.\n'
                                                              f'На столе осталось {total_sweets} конфет.')
            if total_sweets > 0:
                await bot_turn(message)
            else:
                await bot.send_message(message.from_user.id, text=f'Ух ты, ты обыграл искуственный интеллект, поздравляю!')
                total_sweets = 150
                await bot.send_message(message.from_user.id, text=f'Сыграем заново?) Жмакай /start!')
        else:
            await bot.send_message(message.from_user.id, text=f'Возьми-ка поменьше конфет!')
    else:
        await bot.send_message(message.from_user.id, text=f'Эй, нужно ввести число!')






