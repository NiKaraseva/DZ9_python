import bot_turn
import view
from bot_config import dp
from aiogram.types import Message
import model


@dp.message_handler()
async def player_turn(message: Message):
    if model.check_game():
        if message.text.isdigit():
            take = int(message.text)
            if take <= 0:
                await view.take_zero(message)
            elif take >= 29:
                await view.take_over(message)
            elif take > model.get_total():
                await view.take_more_total(message)
            else:
                model.take_sweets(take)
                await view.take_game(message)
                if model.get_total() > 0:
                    await bot_turn.bot_turn(message)
                else:
                    await view.player_win(message)
                    model.new_game()
                    return True
        else:
            await view.take_digit(message)







