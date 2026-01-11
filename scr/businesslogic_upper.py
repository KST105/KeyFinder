from collections import Counter
from itertools import count
from . import businesslogic_lower as bl


def dungeon_movement(direction_movement):
    if direction_movement == "s" or direction_movement == "ы":
        bl.game_map[bl.curren_floor][bl.curren_hall] = "X"
        bl.curren_floor += 1
        bl.game_map[bl.curren_floor][bl.curren_hall] = "H"
    elif direction_movement == "w" or direction_movement == "ц":
        bl.game_map[bl.curren_floor][bl.curren_hall] = "X"
        bl.curren_floor -= 1
        bl.game_map[bl.curren_floor][bl.curren_hall] = "H"
    elif direction_movement == "a" or direction_movement == "ф":
        bl.game_map[bl.curren_floor][bl.curren_hall] = "X"
        bl.curren_hall -= 1
        bl.game_map[bl.curren_floor][bl.curren_hall] = "H"
    elif direction_movement == "d" or direction_movement == "в":
        bl.game_map[bl.curren_floor][bl.curren_hall] = "X"
        bl.curren_hall += 1
        bl.game_map[bl.curren_floor][bl.curren_hall] = "H"

def scan_halls_around(scan_direction):
    counter_scan = 0
    if scan_direction == "a" or scan_direction == "ф":
        bl.curren_hall -= 1
        if bl.game_map[bl.curren_floor][bl.curren_hall] != "?":
            print("Have you explored this hall yet")
        if bl.game_map[bl.curren_floor][bl.curren_hall] != "X":
            print("Have you visited this hall yet")
        bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()
        bl.curren_hall += 1
        counter_scan += 1
        if counter_scan == 5:
            bl.battle_process()
    elif scan_direction == "d" or scan_direction == "в":
        bl.curren_hall += 1
        if bl.game_map[bl.curren_floor][bl.curren_hall] != "?":
            print("Have you explored this hall yet")
        if bl.game_map[bl.curren_floor][bl.curren_hall] != "X":
            print("Have you visited this hall yet")
        bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()
        bl.curren_hall -= 1
        counter_scan += 1
        if counter_scan == 5:
            bl.battle_process()
    elif scan_direction == "s" or scan_direction == "ы":
        if bl.game_map[bl.curren_floor][bl.curren_hall] == bl.game_map[0][5]:
            bl.curren_floor += 1
            bl.game_map[bl.curren_floor][bl.curren_hall] = "O"
            bl.curren_floor -= 1
            counter_scan += 1
            return
        bl.curren_floor += 1
        if bl.game_map[bl.curren_floor][bl.curren_hall] != "?":
            print("Have you explored this hall yet")
        if bl.game_map[bl.curren_floor][bl.curren_hall] != "X":
            print("Have you visited this hall yet")
        bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()
        bl.curren_floor -= 1
        counter_scan += 1
        if counter_scan == 5:
            bl.battle_process()
    elif scan_direction == "w" or scan_direction == "ц":
        bl.curren_floor -= 1
        if bl.game_map[bl.curren_floor][bl.curren_hall] != "?":
            print("Have you explored this hall yet")
        if bl.game_map[bl.curren_floor][bl.curren_hall] != "X":
            print("Have you visited this hall yet")
        bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()
        bl.curren_floor += 1
        counter_scan += 1
        if counter_scan == 5:
            bl.battle_process()
    else:
        counter_scan -= 0.5
        if counter_scan < 0:
            counter_scan = 0
    return

    def battle_process():
        pass