import pygame
from scr.businesslogic_upper import *
from scr.businesslogic_lower import *

pygame.init()

pygame.display.set_caption("Dungeon Explorer")

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
AVAILABLE_MAP_HEIGHT = SCREEN_HEIGHT * 4 // 5
AVAILABLE_MAP_WIDTH = SCREEN_WIDTH * 3 // 5
CELL_SIZE = min(AVAILABLE_MAP_WIDTH // count_hall, AVAILABLE_MAP_HEIGHT // count_floor)
HEIGHT_INDENT_MAP = 100
INDENT_HEIGHT_MASSAGE = 30
INDENT_WIDTH_MAP = (SCREEN_WIDTH // 5 * 3 - CELL_SIZE * count_hall) // 2

MAP_X = INDENT_WIDTH_MAP
MAP_Y = HEIGHT_INDENT_MAP
WIDTH_MAP = CELL_SIZE * count_hall
HEIGHT_MAP = CELL_SIZE * count_floor

map_rect = pygame.Rect(MAP_X, MAP_Y, WIDTH_MAP, HEIGHT_MAP)

MASSAGE_X = map_rect.left
MASSAGE_Y = map_rect.height + HEIGHT_INDENT_MAP + INDENT_HEIGHT_MASSAGE
WIDTH_MASSAGE = map_rect.width
HEIGHT_MASSAGE = (SCREEN_HEIGHT - HEIGHT_MAP - HEIGHT_INDENT_MAP ) / 2

message_rect = pygame.Rect(MASSAGE_X, MASSAGE_Y, WIDTH_MASSAGE, HEIGHT_MASSAGE)

CHARACTER_X = map_rect.right + INDENT_WIDTH_MAP
CHARACTER_Y = map_rect.top
WIDTH_CHARACTER = SCREEN_WIDTH - map_rect.width - INDENT_WIDTH_MAP*3
HEIGHT_CHARACTER = SCREEN_HEIGHT - HEIGHT_INDENT_MAP - INDENT_HEIGHT_MASSAGE

character_rect = pygame.Rect(CHARACTER_X, CHARACTER_Y, WIDTH_CHARACTER , HEIGHT_CHARACTER )

TITLE_X = INDENT_WIDTH_MAP
TITLE_Y = 0
WIDTH_TITLE = WIDTH_MAP + WIDTH_CHARACTER + (character_rect.left - map_rect.right)
HEIGHT_TITLE = HEIGHT_INDENT_MAP - INDENT_HEIGHT_MASSAGE

title_rect = pygame.Rect(INDENT_WIDTH_MAP, TITLE_Y, WIDTH_TITLE, HEIGHT_TITLE)

font = pygame.font.Font(None, 30)

def draw_dungeon():

    for floor in range(count_floor):
        for hall in range(count_hall):

            x = map_rect.x + hall * CELL_SIZE
            y = map_rect.y + floor * CELL_SIZE

            cell = game_map[floor][hall]

            if cell == "#":
                color = (45, 46, 46)

            elif cell == "?":
                color = (75, 75, 75)

            elif cell == "X":
                color = (92,73,57)

            elif cell == "O":
                color = (92,73,57)

            elif cell == "B":
                color = (255, 215, 0)

            elif cell == "Ш":
                color = (180, 50, 50)

            else:
                color = (128, 143, 161)

            pygame.draw.rect(screen, color,(x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen,(20, 20, 20),(x, y, CELL_SIZE, CELL_SIZE),1)

def draw_message():

    pygame.draw.rect(screen,(35, 35, 35), message_rect)

    text_surface = font.render("You found a chest!",True,(255, 255, 255))

    screen.blit(text_surface,(message_rect.x + 10, message_rect.y + 10))

def draw_character_rect():

    pygame.draw.rect(screen,(35, 35, 35), character_rect)

    text_surface = font.render("You found a chest!",True,(255, 255, 255))

    screen.blit(text_surface,(character_rect.x + 10, character_rect.y + 10))

def draw_title_rect():
    pygame.draw.rect(screen,(35, 35, 35), title_rect)

    text_surface = font.render("You found a chest!",True,(255, 255, 255))

    screen.blit(text_surface,(title_rect.x + 10, title_rect.y + 10))

running = True
scanning = False

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                scanning = True
                um.print_massage(um.message_scan_direction)

            elif scanning:

                if event.key == pygame.K_w:
                    scan_halls_around("w")
                    scanning = False

                elif event.key == pygame.K_a:
                    scan_halls_around("a")
                    scanning = False

                elif event.key == pygame.K_s:
                    scan_halls_around("s")
                    scanning = False

                elif event.key == pygame.K_d:
                    scan_halls_around("d")
                    scanning = False

                else:
                    print("Неверное направление!")

            else:

                if event.key == pygame.K_w:
                    dungeon_movement("w")

                elif event.key == pygame.K_a:
                    dungeon_movement("a")

                elif event.key == pygame.K_s:
                    dungeon_movement("s")

                elif event.key == pygame.K_d:
                    dungeon_movement("d")

    draw_dungeon()
    draw_message()
    draw_character_rect()
    draw_title_rect()


    pygame.display.flip()

pygame.quit()