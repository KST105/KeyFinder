from shlex import split

from scr import inventory as inv

hp_recovery = "Нou have restored 3 hp. You have " + str(inv.hp) + " health points."
receiving_damage = "You took" + 1 + "damage. You have " + str(inv.hp) + " health points."