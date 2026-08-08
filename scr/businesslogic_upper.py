from scr import businesslogic_lower as bl
from scr import inventory as inv
from scr import massages_for_user as um
import random

def battle_process():

    enemy_hp = bl.enemy_hp_generator()
    enemy_damage = bl.enemy_damage_generator()
    enemy_type = bl.generation_enemy_type()
    massage_enemy_type = um.meeting_with_enemy(enemy_type)
    attack = bl.enemy_attack_options(enemy_type)
    um.print_massage(massage_enemy_type)

    while inv.hp > 0 and enemy_hp > 0:

        um.print_massage(um.massage_choose_tactics)
        user_input_tactics = bl.user_input()
        user_input_tactics = bl.checking_correct_input(user_input_tactics, "battle_tactical")

        if user_input_tactics == "attack":

            um.print_massage(um.massage_select_attack)
            user_attack = bl.user_input()
            user_attack = bl.checking_correct_input(user_attack, "battle_action_a")
            enemy_attack = bl.enemy_attack_generator(attack)

            if enemy_attack == user_attack:
                enemy_hp -= inv.damage
                inv.hp -= enemy_damage

                um.print_massage(um.receiving_damage(enemy_damage, inv.hp))
                um.print_massage(um.taking_damage_opponent(inv.damage, enemy_hp, enemy_type))

            elif (enemy_attack == "melee" and user_attack == "range") or (enemy_attack == "range" and user_attack == "magic") or (enemy_attack == "magic" and user_attack == "melee"):
                enemy_hp -= inv.damage * 0.5
                inv.hp -= enemy_damage * 2

                um.print_massage(um.receiving_damage(enemy_damage * 2, inv.hp))
                um.print_massage(um.taking_damage_opponent(inv.damage * 0.5, enemy_hp, enemy_type))

            elif (enemy_attack == "melee" and user_attack == "magic") or (enemy_attack == "range" and user_attack == "melee") or (enemy_attack == "magic" and user_attack == "range"):
                enemy_hp -= inv.damage * 2
                inv.hp -= enemy_damage * 0.5

                um.print_massage(um.receiving_damage(enemy_damage * 0.5, inv.hp))
                um.print_massage(um.taking_damage_opponent(inv.damage * 2, enemy_hp, enemy_type))

        else:
            um.print_massage(um.massage_select_defense)
            user_defense  = bl.user_input()
            user_defense = bl.checking_correct_input(user_defense, "battle_action_b")
            enemy_attack = bl.enemy_attack_generator(attack)

            if enemy_attack == user_defense:
                enemy_hp -= inv.damage * 0.5
                um.print_massage(um.taking_damage_opponent(inv.damage * 0.5, enemy_hp, enemy_type))

            else:
                inv.hp -= enemy_damage * 2
                um.print_massage(um.receiving_damage(enemy_damage * 2, inv.hp))
                    
    bl.counter_scan = 0
    return

def dungeon_movement(direction_movement):

    if direction_movement == "s" or direction_movement == "ы":

        bl.game_map[bl.curren_floor][bl.curren_hall] = "X"
        bl.curren_floor += 1

        if bl.game_map[bl.curren_floor][bl.curren_hall] == "?":
            bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()

        if bl.game_map[bl.curren_floor][bl.curren_hall] == "Ш":
            inv.hp -= bl.trap_damage
            um.print_massage(um.receiving_damage(bl.trap_damage, inv.hp))

        elif bl.game_map[bl.curren_floor][bl.curren_hall] == "O":
            um.print_massage(um.massage_empty_hall)

        elif bl.game_map[bl.curren_floor][bl.curren_hall] == "B":
            um.print_massage(um.massage_chest_found)
            bl.reward_from_chest(bl.counter_guarantee_key)

        elif bl.game_map[bl.curren_floor][bl.curren_hall] == "#":

            if bl.curren_floor == 1 and bl.curren_hall == 5:
                bl.game_map[bl.curren_floor][bl.curren_hall] = "H"
                um.print_massage(um.massage_empty_hall)
                return

            bl.curren_floor -= 1
            um.print_massage(um.massage_dead_end)

        bl.game_map[bl.curren_floor][bl.curren_hall] = "H"

    elif direction_movement == "w" or direction_movement == "ц":

        bl.game_map[bl.curren_floor][bl.curren_hall] = "X"
        bl.curren_floor -= 1

        if bl.game_map[bl.curren_floor][bl.curren_hall] == "?":
            bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()

        if bl.game_map[bl.curren_floor][bl.curren_hall] == "Ш":
            inv.hp -= bl.trap_damage
            um.print_massage(um.receiving_damage(bl.trap_damage, inv.hp))

        elif bl.game_map[bl.curren_floor][bl.curren_hall] == "O":
            um.print_massage(um.massage_empty_hall)

        elif bl.game_map[bl.curren_floor][bl.curren_hall] == "B":
            um.print_massage(um.massage_chest_found)
            bl.reward_from_chest(bl.counter_guarantee_key)

        elif bl.game_map[bl.curren_floor][bl.curren_hall] == "#":

            bl.curren_floor += 1
            um.print_massage(um.massage_dead_end)

        bl.game_map[bl.curren_floor][bl.curren_hall] = "H"

    elif direction_movement == "a" or direction_movement == "ф":

        bl.game_map[bl.curren_floor][bl.curren_hall] = "X"
        bl.curren_hall -= 1

        if bl.game_map[bl.curren_floor][bl.curren_hall] == "?":
            bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()

        if bl.game_map[bl.curren_floor][bl.curren_hall] == "Ш":
            inv.hp -= bl.trap_damage
            um.print_massage(um.receiving_damage(bl.trap_damage, inv.hp))

        elif bl.game_map[bl.curren_floor][bl.curren_hall] == "O":
            um.print_massage(um.massage_empty_hall)

        elif bl.game_map[bl.curren_floor][bl.curren_hall] == "B":
            um.print_massage(um.massage_chest_found)
            bl.reward_from_chest(bl.counter_guarantee_key)

        elif bl.game_map[bl.curren_floor][bl.curren_hall] == "#":

            bl.curren_hall += 1
            um.print_massage(um.massage_dead_end)

        bl.game_map[bl.curren_floor][bl.curren_hall] = "H"

    elif direction_movement == "d" or direction_movement == "в":

        bl.game_map[bl.curren_floor][bl.curren_hall] = "X"
        bl.curren_hall += 1

        if bl.game_map[bl.curren_floor][bl.curren_hall] == "?":
            bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()

        if bl.game_map[bl.curren_floor][bl.curren_hall] == "Ш":
            inv.hp -= bl.trap_damage
            um.print_massage(um.receiving_damage(bl.trap_damage, inv.hp))

        elif bl.game_map[bl.curren_floor][bl.curren_hall] == "O":
            um.print_massage(um.massage_empty_hall)

        elif bl.game_map[bl.curren_floor][bl.curren_hall] == "B":
            um.print_massage(um.massage_chest_found)
            bl.reward_from_chest(bl.counter_guarantee_key)

        elif bl.game_map[bl.curren_floor][bl.curren_hall] == "#":

            bl.curren_hall -= 1
            um.print_massage(um.massage_dead_end)

        bl.game_map[bl.curren_floor][bl.curren_hall] = "H"

    elif direction_movement == "q" or direction_movement == "й":

        um.print_massage(um.message_scan_direction)
        scan_direction = bl.user_input()
        scan_direction = bl.checking_correct_input(scan_direction, "scan")
        scan_halls_around(scan_direction)

        return

    bl.counter_scan -= 0.5
    if bl.counter_scan < 0:
        bl.counter_scan = 0

def scan_halls_around(scan_direction):

    while scan_direction in ("w", "a", "s", "d", "ц", "ф", "ы", "в", "x", "ч"):

        if scan_direction in ("w", "a", "s", "d", "ц", "ф", "ы", "в"):
            bl.counter_scan += 1

            if bl.counter_scan == bl.max_counter_scan:
                um.print_massage(um.massage_beginnin_battle)
                battle_process()

            if scan_direction in ("a", "ф"):
                bl.curren_hall -= 1

                if bl.game_map[bl.curren_floor][bl.curren_hall] == "?":
                    bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()

                else:
                    um.print_massage(um.massage_repeat_research)

                bl.curren_hall += 1
                return

            elif scan_direction in ("d", "в"):
                bl.curren_hall += 1

                if bl.game_map[bl.curren_floor][bl.curren_hall] == "?":
                    bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()

                else:
                    um.print_massage(um.massage_repeat_research)

                bl.curren_hall -= 1
                return

            elif scan_direction in ("s", "ы"):
                bl.curren_floor += 1

                if bl.game_map[bl.curren_floor][bl.curren_hall] == "?":
                    bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()

                    if bl.game_map[bl.curren_floor][bl.curren_hall] == "#" and (
                            bl.curren_floor - 1 == 0 and bl.curren_hall == 5):
                        bl.game_map[bl.curren_floor][bl.curren_hall] = "0"

                elif bl.game_map[bl.curren_floor][bl.curren_hall] == "X":
                    um.print_massage(um.massage_repeat_visit)

                else:
                    um.print_massage(um.massage_repeat_research)

                bl.curren_floor -= 1
                return

            elif scan_direction in ("w", "ц"):
                bl.curren_floor -= 1

                if bl.game_map[bl.curren_floor][bl.curren_hall] == "?":
                    bl.game_map[bl.curren_floor][bl.curren_hall] = bl.exploring_room()

                else:
                    um.print_massage(um.massage_repeat_research)

                bl.curren_floor += 1
                return

    return
