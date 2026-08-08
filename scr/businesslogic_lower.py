import random
from scr import inventory as inv
from scr import massages_for_user as um
from scr import businesslogic_lower as bl

counter_guarantee_chest = 0
value_guaranteed_chest = 4
counter_guarantee_key = 0
value_guarantee_key = 4
size_dungeon = 11
curren_floor = 0
curren_hall = 5
counter_scan = 0
max_counter_scan = 6
trap_damage = 15
triumphant_number_keys = 5

probability_appearing_objects = [3, 3.5, 1.5, 2]
probability_appearing_rewards = [1, 3]

map_objects = ["trap", "nothing", "chest", "impasse"]
probability_reward_type = ["key", "potion"]
probability_enemy_type = ["Dark Elf", "Goblin Marauder", "Cursed Knight"]

def reward_from_chest(counter_guarantee_key):
    counter_guarantee_key += 1

    if counter_guarantee_key == value_guarantee_key:
        inv.key += 1
        bl.counter_guarantee_key = 0

        return um.print_massage(um.found_key)

    reward_chest = random.choices(probability_reward_type, weights=probability_appearing_rewards)[0]

    if reward_chest == "key":
        inv.key += 1
        bl.counter_guarantee_key = 0

        um.print_massage(f"You have found the key. There are still {5 - int(inv.key)} left to find.")

    else:
        number = random.randint(0, 1)

        if number == 0:
            inv.health_potion += 1
            um.print_massage(f"You have found a healing potion. current count: {inv.health_potion}.")

        else:
            inv.power_potion += 1
            (um.print_massage(f"You have found a power potion. current count: {inv.power_potion}."))

def enemy_attack_options(type_enemy):

    if type_enemy == "Dark Elf":
        dark_elf_attack = ["range", "magic"]
        return dark_elf_attack

    elif type_enemy == "Goblin Marauder":
        goblin_marauder_attack = ["melee ", "range"]
        return goblin_marauder_attack

    elif type_enemy == "Cursed Knight":
        cursed_knight_attack = ["magic", "melee"]
        return cursed_knight_attack

def enemy_attack_generator(attack):

    probability_attack = [2, 1]
    result_investigation = random.choices(attack, weights=probability_attack)[0]
    return result_investigation

def map_generation():
    game_map = [["#" for hall in range(size_dungeon)] for floor in range(size_dungeon)]

    for floor in range(1, size_dungeon-1):
        for hall in range(1, size_dungeon-1):
            game_map[floor][hall] = "?"

    game_map[curren_floor][curren_hall] = "H"

    return game_map

game_map = map_generation()

def verification_guaranteed_chest(result):

    if result != "chest":
        bl.counter_guarantee_chest += 1

        if bl.counter_guarantee_chest == value_guaranteed_chest:
            result = "chest"
            bl.counter_guarantee_chest = 0
            return result

        return result

def exploring_room():

    result_investigation = random.choices(map_objects, weights=probability_appearing_objects)[0]

    if result_investigation == "trap":
        result = "Ш"
        return result

    elif result_investigation == "nothing":
        result = "O"
        return result

    elif result_investigation == "chest":
        result = "B"
        return result

    elif result_investigation == "impasse":
        result = "#"
        return result




def show_map():

    for i in range(0, size_dungeon):
        for j in range(0, size_dungeon):
            print(game_map[i][j], end=" ")
        print(end="\n")

    return ""

def enemy_hp_generator():

    enemy_hp = random.randint(30, 70)
    return enemy_hp

def enemy_damage_generator():

    enemy_damage = random.randint(10, 30)
    return enemy_damage

def hit(attack_damage, defenders_hp ):

        defenders_hp -= attack_damage

def use_health_potion():

    inv.health_potion -= 1
    inv.hp += 25

    if inv.hp > 100:
        inv.hp = 100


def generation_enemy_type():

    enemy_type = random.choice(probability_enemy_type)
    return enemy_type

def use_power_potion():

    inv.damage += 5
    if inv.damage > 50:
        inv.damage = 100

def user_input():

    inp = input(">>>").strip()

    return inp


def checking_correct_input(inp, type):

    if type == "move":

        while inp not in ("w", "a", "s", "d", "ц", "ф", "ы", "в", "q", "й"):
            um.print_massage(um.message_incorrect_direction_movement)
            inp = input(">>>").strip()

    elif type == "scan":

        while inp not in ("w", "a", "s", "d", "ц", "ф", "ы", "в"):
            um.print_massage(um.message_incorrect_direction_scan)
            inp = input(">>>").strip()

    elif type == "battle_tactical":

        while inp not in ("attack", "defense"):
            um.print_massage(um.massage_incorrect_choose_tactics)
            inp = input(">>>").strip()

    elif type == "battle_action_a":

        while inp not in ("melee", "range", "magic"):
            um.print_massage(um.massage_select_incorrect_attack)
            inp = input(">>>").strip()

    elif type == "battle_action_b":

        while inp not in ("melee", "range", "magic"):
            um.print_massage(um.massage_select_incorrect_defense)
            inp = input(">>>").strip()

    return inp