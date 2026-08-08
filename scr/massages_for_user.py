from scr import inventory as inv
from scr import businesslogic_lower as bl

def print_massage(massage):
    return print(massage)

def meeting_with_enemy(enemy):

    return f"While exploring another dungeon room too carelessly, you attracted too much attention. {enemy} has spotted you and is preparing for battle."

def hp_recovery(hp):

    return f"Нou have restored 3 hp. You have {str(hp)} health points."

def receiving_damage(dm, hp):

    return f"You took {str(dm)} damage. You have {str(hp)} health points."

def taking_damage_opponent(dm, hp, enemy):

    return f"You have dealt damage of {str(dm)}. {enemy} health points of {str(hp)}."

massage_choose_tactics = "Choose your battle tactics for the next turn. (attack/defense)"

massage_select_attack = "Select attack type (melee/range/magic)"

massage_select_defense = "Select parry type (melee/range/magic)"

massage_beginnin_battle = "The battle begins..."

massage_repeat_visit = "Have you visited this hall yet"

massage_repeat_research = "Have you explored this hall yet"

massage_empty_hall = "This hall is empty. You haven’t found anything."

massage_chest_found = "Have you found the chest"

massage_dead_end = "You’ve reached a dead end. There’s no further path."

found_key = f"You have found the key. There are still {5 - int(inv.key)} left to find."

number_healing_potions = f"You have found a healing potion. current count: {int(inv.health_potion)}."

number_power_potions = f"You have found a power potion. current count: {int(inv.power_potion)}."

message_movement_direction = f"Select the movement direction (WASD). To scan, press (Q)."

message_scan_direction = f"Select the movement scan (WASD)."

message_incorrect_direction_movement = f"Choose the correct direction of movement (WASD) or cast the scanning spell (Q)."

message_incorrect_direction_scan = f"Choose the correct direction of scan (WASD)."

massage_incorrect_choose_tactics = "Choose correct your battle tactics for the next turn. (attack/defense)"

massage_select_incorrect_attack = "Select correct attack type (melee/range/magic)"

massage_select_incorrect_defense = "Select correct parry type (melee/range/magic)"