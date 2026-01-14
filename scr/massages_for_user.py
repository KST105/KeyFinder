from scr import inventory as inv

def print_massage(massage):
    return print(massage)

def meeting_with_enemy(enemy):
    massage = "While exploring another dungeon room too carelessly, you attracted too much attention. " + enemy + " has spotted you and is preparing for battle."
    return massage

def hp_recovery(hp):
    massage = "Нou have restored 3 hp. You have " + str(hp) + " health points."
    return massage

def receiving_damage(dm, hp):
    massage = "You took" + str(dm) + "damage. You have " + str(hp) + " health points."
    return massage

