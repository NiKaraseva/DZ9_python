from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_start = KeyboardButton(text='/start')
btn_new_game = KeyboardButton(text='/new_game')
btn_help = KeyboardButton(text='/help')
btn_level = KeyboardButton(text='/level')

kb_menu.row(btn_start, btn_new_game)
kb_menu.add(btn_help)
kb_menu.add(btn_level)
