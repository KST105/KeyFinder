import random

counter_guarantee_box = 0
counter_guarantee_key = 0

probability_appearing_objects = [2.5, 3, 1, 2]
map_objects = ["trap", "nothing", "loot box", "impasse"]

def map_generation():
    game_map = [["#" if floor == 10 or (floor == 0 and not hall == 5) or hall == 0 or hall == 10 and not floor == 0 and not hall == 6 else "?" for hall in range(11)] for floor in range(11)]

    return game_map

game_map = map_generation()

curren_floor = 0
curren_hall = 5


def exploring_room():

    result_investigation = random.choices(map_objects, weights=probability_appearing_objects)[0]

    if result_investigation == "trap":
        result = "Ш"
    elif result_investigation == "nothing":
        result = "O"
    elif result_investigation == "loot box":
        result = "B"
    elif result_investigation == "impasse":
        result = "#"

    return result

def show_map():
    for i in range(0, 11):
        for j in range(0, 11):
            print(game_map[i][j], end=" ")
        print(end="\n")
    return ""

