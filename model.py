total_sweets = 150
player = ''
new_game = False

def new_game():
    global new_game
    if new_game:
        new_game = False
    else:
        new_game = True

def get_total():
    global total_sweets
    return total_sweets

def take_sweets(take: int):
    global total_sweets
    total_sweets -= take





