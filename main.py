from scr.businesslogic_upper import *
from scr.businesslogic_lower import *


user_input = 0


while user_input != "exit":

    print(bl.show_map())
    move = bl.user_input()
    move = bl.checking_correct_input(move, "move")
    dungeon_movement(move)







