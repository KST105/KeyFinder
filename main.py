from scr.gamelogic_upper import *
from scr.gamelogic_ui import *

running = True
scanning = False
destruction = False

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                scanning = True
                current_message = message_scan_direction

            elif scanning:

                if event.key == pygame.K_w:
                    current_message = scan_halls_around("w")
                    scanning = False

                elif event.key == pygame.K_a:
                    current_message = scan_halls_around("a")
                    scanning = False

                elif event.key == pygame.K_s:
                    current_message = scan_halls_around("s")
                    scanning = False

                elif event.key == pygame.K_d:
                    current_message = scan_halls_around("d")
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

                elif event.key == pygame.K_a:
                    current_message = destroy_object("a")
                    destruction = False

                elif event.key == pygame.K_s:
                    current_message = destroy_object("s")
                    destruction = False

                elif event.key == pygame.K_d:
                    current_message = destroy_object("d")
                    destruction = False

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









