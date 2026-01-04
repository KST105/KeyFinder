
def map_generation():
    game_map = [["#" if floor == 0 or (floor == 10 and not hall == 5) or hall == 0 or hall == 10 and not floor == 10 and not hall == 6 else "?" for hall in range(11)] for floor in range(11)]

    return game_map

