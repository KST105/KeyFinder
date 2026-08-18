import pygame
from scr.gamelogic_lower import *
from scr.massages_player import *

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
current_message = "Добро пожаловать в подземелье!"

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

CHARACTER_CONTROL_Y = character_rect.y + character_rect.height * 2/3
CHARACTER_INFO_HEIGHT =  character_rect.height * 2/3

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

def draw_message(current_message):

    pygame.draw.rect(screen, (35, 35, 35), message_rect)

    text_message = font.render(current_message, True, (255, 255, 255))

    screen.blit( text_message, (message_rect.x + 10, message_rect.y + 10))

def draw_character_rect():

    text_character_info = f"HP: {str(inv.hp)}\n\nWARINESS: {str(inv.counter_scan)} out of {str(inv.max_counter_scan)}\n\nDAMAGE:{str(inv.damage)}\n\n"

    text_character_inventory = f"HEALTH POTION: {str(inv.health_potion)}\n\nPOWER POTION: {str(inv.power_potion)}\n\nKEY: {str(inv.key)}"

    pygame.draw.rect(screen,(35, 35, 35), character_rect)

    text_control = font.render(text_control_key,True,(255, 255, 255))
    screen.blit(text_control,(character_rect.x + 30, CHARACTER_CONTROL_Y + 30))
    pygame.draw.rect(screen, (20, 20, 20), (character_rect.x, CHARACTER_CONTROL_Y, character_rect.width, character_rect.height * 1/3 + 1), 1)

    text_character = font.render(text_character_info, True, (255, 255, 255))
    screen.blit(text_character, (character_rect.x + 30, character_rect.y + 30))
    pygame.draw.rect(screen, (20, 20, 20),(character_rect.x, character_rect.y, character_rect.width/2, CHARACTER_INFO_HEIGHT), 1)

    text_character_inv = font.render(text_character_inventory, True, (255, 255, 255))
    screen.blit(text_character_inv, (character_rect.x + (character_rect.width / 2) + 30, character_rect.y + 30))
    pygame.draw.rect(screen, (20, 20, 20),(character_rect.x + (character_rect.width / 2), character_rect.y, character_rect.width / 2 + 1, CHARACTER_INFO_HEIGHT), 1)



def draw_title_rect():
    pygame.draw.rect(screen,(35, 35, 35), title_rect)

    text_surface = font.render("Заглушка",True,(255, 255, 255))

    screen.blit(text_surface,(title_rect.x + 10, title_rect.y + 10))

