import random

curren_floor = 0
curren_hall = 5

counter_guarantee_box = 0
counter_guarantee_key = 0

probability_appearing_objects = [0.3, 0.35, 0.15, 0.2]
map_objects = ["trap", "nothing", "loot box", "impasse"]

def map_generation():
    game_map = [["#" if floor == 10 or (floor == 0 and not hall == 5) or hall == 0 or hall == 10 and not floor == 0 and not hall == 6 else "?" for hall in range(11)] for floor in range(11)]

    return game_map

game_map = map_generation()

def dungeon_movement(direction_movement):


def exploring_room(direction_research_floor, direction_research_hall):

    result_investigation = random.sample(map_objects)

    if result_investigation == "trap":
        game_map[direction_research_floor][direction_research_hall] = "Ш"
    elif result_investigation == "nothing":
        game_map[direction_research_floor][direction_research_hall] = "O"
    elif result_investigation == "loot box":
        game_map[direction_research_floor][direction_research_hall] = "B"
    else:
        game_map[direction_research_floor][direction_research_hall] = "#"
        result_investigation = "#"

    return result_investigation