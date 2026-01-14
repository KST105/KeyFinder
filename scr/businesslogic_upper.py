from scr import businesslogic_lower as bl
from scr import inventory as inv
from scr import massages_for_user as um



def battle_process():

    enemy_hp = bl.enemy_hp_generator()
    enemy_damage = bl.enemy_damage_generator()
    enemy_type = bl.generation_enemy_type()
    massage_enemy_type = um.meeting_with_enemy(enemy_type)
    attack = bl.enemy_attack_options(enemy_type)
    um.print_massage(massage_enemy_type)

    while inv.hp > 0 and enemy_hp > 0:
        um.print_massage(um.massage_choose_tactics)
        user_input_tactics = str(input) # временное решение (будет функция пользовательского ввода)

        if user_input_tactics != "attack" or user_input_tactics != "defense":
            continue

        if user_input_tactics == "attack":

            um.print_massage(um.massage_select_attack)
            user_attack = str(input) # временное решение (будет функция пользовательского ввода)
            if user_attack != "melee" or user_attack != "ranged" or user_attack != "magic":
                continue

            enemy_attack = bl.enemy_attack_generator(attack)
            if enemy_attack == user_attack:
                enemy_hp -= inv.damage
                inv.hp -= enemy_damage
            elif (enemy_attack == "melee" and user_attack == "ranged") or (enemy_attack == "ranged" and user_attack == "magic") or (enemy_attack == "magic" and user_attack == "melee"):
                enemy_hp -= inv.damage * 0.5
                inv.hp -= enemy_damage * 2
            elif (enemy_attack == "melee" and user_attack == "magic") or (enemy_attack == "ranged" and user_attack == "melee") or (enemy_attack == "magic" and user_attack == "ranged"):
                enemy_hp -= inv.damage * 2
                inv.hp -= enemy_damage * 0.5

        else:
            um.print_massage(um.massage_select_defense)
            user_defense  = str(input) # временное решение (будет функция пользовательского ввода)
            if user_defense != "melee" or user_defense != "ranged" or user_defense !="magic":
                continue

            enemy_attack = bl.enemy_attack_generator(attack)
            if enemy_attack == user_defense:
                enemy_hp -= inv.damage * 0.5
            else:
                inv.hp -= enemy_damage * 2
                    
    bl.counter_scan = 0
    return

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
