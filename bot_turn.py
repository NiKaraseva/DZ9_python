from random import randint as rnd
import view
import model



async def bot_turn(message):
    total = model.get_total()
    if model.get_bot_level() == 'Light':
        if total <= 28:
            take_sweets_bot = total
        else:
            take_sweets_bot = rnd(1, 28)
    else:
        take_sweets_bot = total % 29 if total % 29 != 0 else rnd(1, 28)
    model.take_sweets(take_sweets_bot)
    await view.bot_game(message, take_sweets_bot)
    if model.get_total() > 0:
        await view.player_turn_message(message)
    else:
        await view.bot_win(message)
        model.new_game()
        return True