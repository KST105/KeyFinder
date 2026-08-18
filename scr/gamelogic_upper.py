from scr import gamelogic_lower as gl_l
from scr import inventory as inv
from scr import massages_player as mp
from scr import gamelogic_ui as pg


def battle_process():

    enemy_hp = gl_l.enemy_hp_generator()
    enemy_damage = gl_l.enemy_damage_generator()
    enemy_type = gl_l.generation_enemy_type()
    massage_enemy_type = mp.meeting_with_enemy(enemy_type)
    attack = gl_l.enemy_attack_options(enemy_type)
    pg.current_message = massage_enemy_type

    while inv.hp > 0 and enemy_hp > 0:

        mp.print_massage(mp.massage_choose_tactics)
        user_input_tactics = gl_l.user_input()
        user_input_tactics = gl_l.checking_correct_input(user_input_tactics, "battle_tactical")

        if user_input_tactics == "attack":

            mp.print_massage(mp.massage_select_attack)
            user_attack = gl_l.user_input()
            user_attack = gl_l.checking_correct_input(user_attack, "battle_action_a")
            enemy_attack = gl_l.enemy_attack_generator(attack)

            if enemy_attack == user_attack:
                enemy_hp -= inv.damage
                inv.hp -= enemy_damage

                pg.current_message = mp.receiving_damage(enemy_damage, inv.hp)
                pg.current_message = mp.taking_damage_opponent(inv.damage, enemy_hp, enemy_type)

            elif (enemy_attack == "melee" and user_attack == "range") or (enemy_attack == "range" and user_attack == "magic") or (enemy_attack == "magic" and user_attack == "melee"):
                enemy_hp -= inv.damage * 0.5
                inv.hp -= enemy_damage * 2

                pg.current_message = mp.receiving_damage(enemy_damage * 2, inv.hp)
                pg.current_message = mp.taking_damage_opponent(inv.damage * 0.5, enemy_hp, enemy_type)

            elif (enemy_attack == "melee" and user_attack == "magic") or (enemy_attack == "range" and user_attack == "melee") or (enemy_attack == "magic" and user_attack == "range"):
                enemy_hp -= inv.damage * 2
                inv.hp -= enemy_damage * 0.5

                pg.current_message = mp.receiving_damage(enemy_damage * 0.5, inv.hp)
                pg.current_message = mp.taking_damage_opponent(inv.damage * 2, enemy_hp, enemy_type)

        else:
            mp.print_massage(mp.massage_select_defense)
            user_defense  = gl_l.user_input()
            user_defense = gl_l.checking_correct_input(user_defense, "battle_action_b")
            enemy_attack = gl_l.enemy_attack_generator(attack)

            if enemy_attack == user_defense:
                enemy_hp -= inv.damage * 0.5
                pg.current_message = mp.taking_damage_opponent(inv.damage * 0.5, enemy_hp, enemy_type)

            else:
                inv.hp -= enemy_damage * 2
                mp.receiving_damage(enemy_damage * 2, inv.hp)
                    
    gl_l.counter_scan = 0
    return

def dungeon_movement(direction_movement):

    if direction_movement == "s":

        gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "X"
        gl_l.curren_floor += 1

        if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "?":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = gl_l.exploring_room()

            inv.counter_scan -= 0.5
            if inv.counter_scan < 0:
                inv.counter_scan = 0

        if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "Ш":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            inv.hp -= gl_l.trap_damage
            return mp.receiving_damage(gl_l.trap_damage, inv.hp)

        elif gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "O":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            return mp.massage_empty_hall

        elif gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "B":
            gl_l.reward_from_chest(gl_l.counter_guarantee_key)
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            return mp.massage_chest_found

        elif gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] in ("#","*"):

            gl_l.curren_floor -= 1
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            return mp.massage_dead_end

        gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"

    elif direction_movement == "w":

        gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "X"
        gl_l.curren_floor -= 1

        if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "?":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = gl_l.exploring_room()

            inv.counter_scan -= 0.5
            if inv.counter_scan < 0:
                inv.counter_scan = 0

        if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "Ш":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            inv.hp -= gl_l.trap_damage
            return mp.receiving_damage(gl_l.trap_damage, inv.hp)

        elif gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "O":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            return mp.massage_empty_hall

        elif gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "B":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            gl_l.reward_from_chest(gl_l.counter_guarantee_key)
            return mp.massage_chest_found

        elif gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall]in ("#","*"):

            gl_l.curren_floor += 1
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            return mp.massage_dead_end

        gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"

    elif direction_movement == "a":

        gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "X"
        gl_l.curren_hall -= 1

        if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "?":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = gl_l.exploring_room()

            inv.counter_scan -= 0.5
            if inv.counter_scan < 0:
                inv.counter_scan = 0

        if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "Ш":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            inv.hp -= gl_l.trap_damage
            return mp.receiving_damage(gl_l.trap_damage, inv.hp)

        elif gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "O":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            return mp.massage_empty_hall

        elif gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "B":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            gl_l.reward_from_chest(gl_l.counter_guarantee_key)
            return mp.massage_chest_found

        elif gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] in ("#","*"):

            gl_l.curren_hall += 1
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            return mp.massage_dead_end

        gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"

    elif direction_movement == "d":

        gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "X"
        gl_l.curren_hall += 1

        if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "?":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = gl_l.exploring_room()

            inv.counter_scan -= 0.5
            if inv.counter_scan < 0:
                inv.counter_scan = 0

        if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "Ш":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            inv.hp -= gl_l.trap_damage
            return mp.receiving_damage(gl_l.trap_damage, inv.hp)

        elif gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "O":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            return mp.massage_empty_hall

        elif gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "B":
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            gl_l.reward_from_chest(gl_l.counter_guarantee_key)
            return mp.massage_chest_found

        elif gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] in ("#","*"):

            gl_l.curren_hall -= 1
            gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"
            return mp.massage_dead_end

        gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = "H"


def scan_halls_around(scan_direction):

    while scan_direction in ("w", "a", "s", "d"):

        if scan_direction in ("w", "a", "s", "d"):
            inv.counter_scan += 1

            if inv.counter_scan >= inv.max_counter_scan:
                mp.print_massage(mp.massage_beginnin_battle)
                battle_process()

            if scan_direction == "a":
                gl_l.curren_hall -= 1

                if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "?":
                    gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = gl_l.exploring_room()

                else:
                    gl_l.curren_hall += 1
                    return mp.massage_repeat_research

                gl_l.curren_hall += 1
                return

            elif scan_direction == "d":
                gl_l.curren_hall += 1

                if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "?":
                    gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = gl_l.exploring_room()

                else:
                    gl_l.curren_hall -= 1
                    return mp.massage_repeat_research

                gl_l.curren_hall -= 1
                return

            elif scan_direction == "s":
                gl_l.curren_floor += 1

                if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "?":
                    gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = gl_l.exploring_room()

                else:
                    gl_l.curren_floor -= 1
                    return mp.massage_repeat_research

                gl_l.curren_floor -= 1
                return

            elif scan_direction == "w":
                gl_l.curren_floor -= 1

                if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] == "?":
                    gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = gl_l.exploring_room()

                else:
                    gl_l.curren_floor += 1
                    return mp.massage_repeat_research

                gl_l.curren_floor += 1
                return

    return

def destroy_object(direction):

    while direction in ("w", "a", "s", "d"):

        if direction == "a":
            gl_l.curren_hall -= 1

            if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] in ("#","Ш"):
                gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = gl_l.exploring_room_in_destruction()
                gl_l.curren_hall += 1
                return mp.massage_beginnin_battle, battle_process()

            else:
                gl_l.curren_hall += 1
                return mp.message_invalid_destruction_object

        elif direction == "d":
            gl_l.curren_hall += 1

            if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] in ("#","Ш"):
                gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = gl_l.exploring_room_in_destruction()
                gl_l.curren_hall -= 1
                return mp.massage_beginnin_battle, battle_process()

            else:
                gl_l.curren_hall -= 1
                return mp.message_invalid_destruction_object

        elif direction == "s":
            gl_l.curren_floor += 1

            if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] in ("#","Ш"):
                gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = gl_l.exploring_room_in_destruction()
                gl_l.curren_floor -= 1
                return mp.massage_beginnin_battle, battle_process()

            else:
                gl_l.curren_floor -= 1
                return mp.message_invalid_destruction_object

        elif direction == "w":
            gl_l.curren_floor -= 1

            if gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] in ("#","Ш"):
                gl_l.game_map[gl_l.curren_floor][gl_l.curren_hall] = gl_l.exploring_room_in_destruction()
                gl_l.curren_floor += 1
                return mp.massage_beginnin_battle, battle_process()

            else:
                gl_l.curren_floor += 1
                return mp.message_invalid_destruction_object
