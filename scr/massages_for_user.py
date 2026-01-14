from scr import inventory as inv

def print_massage(massage):
    return print(massage)

def meeting_with_enemy(enemy):
    massage = "While exploring another dungeon room too carelessly, you attracted too much attention. " + enemy + " has spotted you and is preparing for battle."
    return massage

hp_recovery = "Нou have restored 3 hp. You have " + str(inv.hp) + " health points."
receiving_damage = "You took" + "1" + "damage. You have " + str(inv.hp) + " health points."

