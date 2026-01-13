from scr import businesslogic_lower as bl
from scr import inventory as inv

"""
def battle_process():
    enemy_hp = bl.enemy_hp_generator()
    enemy_damage = bl.enemy_damage_generator()
    enemy_type = bl.generation_enemy_type()

    while inv.hp <= 0 or enemy_hp <= 0:
    
    bl.counter_scan = 0
"""



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
    if scan_direction == "w" or "a" or "s" or "d" or "ц" or "ф" or "ы" or "в":

        bl.counter_scan += 1
        if bl.counter_scan == 5:
            #battle_process()#
            print("бой начинается")

        if scan_direction == "a" or scan_direction == "ф":
            bl.curren_hall -= 1

            if bl.game_map[bl.curren_floor][bl.curren_hall] == "?" :
                bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()

            elif bl.game_map[bl.curren_floor][bl.curren_hall] == "X":
                print("Have you visited this hall yet")

            else:
                print("Have you explored this hall yet")

            bl.curren_hall += 1
            return

        elif scan_direction == "d" or scan_direction == "в":
            bl.curren_hall += 1

            if bl.game_map[bl.curren_floor][bl.curren_hall] == "?":
                bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()

            elif bl.game_map[bl.curren_floor][bl.curren_hall] == "X":
                print("Have you visited this hall yet")

            else:
                print("Have you explored this hall yet")

            bl.curren_hall -= 1
            return

        elif scan_direction == "s" or scan_direction == "ы":
            bl.curren_floor += 1

            if bl.game_map[bl.curren_floor][bl.curren_hall] == "?":
                bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()
                if bl.game_map[bl.curren_floor][bl.curren_hall] == "#" and (bl.curren_floor - 1 == 0 and bl.curren_hall == 5):
                    bl.game_map[bl.curren_floor][bl.curren_hall] = "0"

            elif bl.game_map[bl.curren_floor][bl.curren_hall] == "X":
                print("Have you visited this hall yet")

            else:
                print("Have you explored this hall yet")

            bl.curren_floor -= 1
            return

        elif scan_direction == "w" or scan_direction == "ц":

            bl.curren_floor -= 1
            if bl.game_map[bl.curren_floor][bl.curren_hall] == "?":
                bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()
            elif bl.game_map[bl.curren_floor][bl.curren_hall] == "X":
                print("Have you visited this hall yet")
            else:
                print("Have you explored this hall yet")

            bl.curren_floor -= 1
            return

    else:
        bl.counter_scan -= 0.5
        if bl.counter_scan < 0:
            bl.counter_scan = 0
    return
