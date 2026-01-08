import random

counter_guarantee_box = 0
counter_guarantee_key = 0

probability_appearing_objects = [2.5, 3, 1, 2]
map_objects = ["trap", "nothing", "loot box", "impasse"]
size_dungeon = 11 #odd value
curren_floor = 0
curren_hall = 5

def map_generation():
    game_map = [["#" for hall in range(size_dungeon)] for floor in range(size_dungeon)]

    for floor in range(1, 10):
        for hall in range(1, 10):
            game_map[floor][hall] = "?"

    game_map[curren_floor][curren_hall] = "H"
    return game_map

game_map = map_generation()

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

