from scr.gamelogic_upper import *
from scr.gamelogic_ui import *

running = True
scanning = False
destruction = False
combat_action = False
battle_state = "tactic"

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if combat_action:

                current_message = massage_beginnin_battle

                if battle_state == "tactic":

                    if event.key == pygame.K_1:
                        battle_tactic = "attack"
                        battle_state = "action"

                    elif event.key == pygame.K_2:
                        battle_tactic = "defence"
                        battle_state = "action"

                elif battle_state == "action":

                    if event.key == pygame.K_1:
                        battle_action = "melee"

                    elif event.key == pygame.K_2:
                        battle_action = "range"

                    elif event.key == pygame.K_3:
                        battle_action = "magic"

                    battle_round(enemy, battle_tactic, battle_action)
                    battle_state = "tactic"

            elif event.key == pygame.K_q:
                scanning = True
                current_message = message_scan_direction

            elif scanning:

                if event.key == pygame.K_w:

                    result = scan_halls_around("w")

                    if result is True:

                        current_message = enemy_generator()
                        combat_action = True
                        battle_state = "tactic"

                    else:
                        current_message = result

                    scanning = False

                elif event.key == pygame.K_a:

                    result = scan_halls_around("a")

                    if result is True:

                        current_message = enemy_generator()
                        combat_action = True
                        battle_state = "tactic"

                    else:
                        current_message = result

                    scanning = False

                elif event.key == pygame.K_s:

                    result = scan_halls_around("s")

                    if result is True:

                        current_message = enemy_generator()
                        combat_action = True
                        battle_state = "tactic"

                    else:
                        current_message = result

                    scanning = False

                elif event.key == pygame.K_d:

                    result = scan_halls_around("d")

                    if result is True:

                        current_message = enemy_generator()
                        combat_action = True
                        battle_state = "tactic"

                    else:
                        current_message = result

                    scanning = False

                elif event.key == pygame.K_x:
                    scanning = False

            elif event.key == pygame.K_r:
                destruction = True
                current_message = message_destruction_direction

            elif destruction:

                if event.key == pygame.K_w:
                    current_message = destroy_object("w")
                    destruction = False
                    combat_action = True

                elif event.key == pygame.K_a:
                    current_message = destroy_object("a")
                    destruction = False
                    combat_action = True

                elif event.key == pygame.K_s:
                    current_message = destroy_object("s")
                    destruction = False
                    combat_action = True

                elif event.key == pygame.K_d:
                    current_message = destroy_object("d")
                    destruction = False
                    combat_action = True

                elif event.key == pygame.K_x:
                    destruction = False

            else:

                if event.key == pygame.K_w:

                    current_message = dungeon_movement("w")

                elif event.key == pygame.K_a:

                    current_message = dungeon_movement("a")

                elif event.key == pygame.K_s:

                    current_message = dungeon_movement("s")

                elif event.key == pygame.K_d:

                    current_message = dungeon_movement("d")

                elif event.key == pygame.K_h:

                    current_message = use_health_potion()

                elif event.key == pygame.K_g:

                    current_message = use_power_potion()

    draw_dungeon()
    draw_title_rect()
    draw_character_rect()
    draw_message(current_message)

    pygame.display.flip()

pygame.quit()









