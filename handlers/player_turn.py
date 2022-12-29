from bot_config import bot, dp
from aiogram.types import Message
import handlers



@dp.message_handler()
async def player_turn(message: Message):
    global total_sweets
    if message.text.isdigit():
        if 0 < int(message.text) < 29:
            total_sweets -= int(message.text)
            await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name} взял со стола '
                                                              f'{message.text} конфет.\n'
                                                              f'На столе осталось {total_sweets} конфет.')
            if total_sweets > 0:
                await handlers.bot_turn(message)
            else:
                await bot.send_message(message.from_user.id, text=f'Да ты конфетный супермен! Поздравляю с выигрышем!')
                total_sweets = 150
                await bot.send_message(message.from_user.id, text=f'Сыграем заново?) Жмакай /start!')
        else:
            await bot.send_message(message.from_user.id, text=f'Возьми-ка поменьше конфет!')
    else:
        await bot.send_message(message.from_user.id, text=f'Эй, нужно ввести число!')