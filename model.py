total_sweets = 150
player = ''
game = False
bot_level = 'Light'


def new_game():
    global game
    global total_sweets
    if game:
        game = False
    else:
        total_sweets = 150
        game = True

def check_game():
    global game
    return game

def get_total():
    global total_sweets
    return total_sweets

def take_sweets(take: int):
    global total_sweets
    total_sweets -= take


def change_level():
    global bot_level
    if bot_level == 'Light':
        bot_level = 'Hard'
    else:
        bot_level = 'Light'


def get_bot_level():
    global bot_level
    return bot_level
