from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

kb_inline = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_print = []
draw = ['Орел', 'Решка']

for toss in draw:
    btn_print.append(KeyboardButton(text=toss))


kb_inline.row(*btn_print)