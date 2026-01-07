import businesslogic_lower as bl



def scan_halls_around(scan_direction):
    if scan_direction == "a" or scan_direction == "ф":
        bl.curren_hall -= 1
        bl.exploring_room(bl.curren_floor, bl.curren_hall)
        l.curren_hall += 1
    elif scan_direction == "d" or scan_direction == "в":
        bl.curren_hall += 1
        bl.exploring_room(bl.curren_floor, bl.curren_hall)
        bl.curren_hall -= 1
    elif scan_direction == "s" or scan_direction == "ы":
        bl.curren_floor += 1
        bl.exploring_room(bl.curren_floor, bl.curren_hall)
        bl.curren_floor -= 1
    elif scan_direction == "w" or scan_direction == "ц":
        bl.curren_floor -= 1
        bl.exploring_room(bl.curren_floor, bl.curren_hall)
        bl.curren_floor += 1



