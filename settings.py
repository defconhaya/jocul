from pygame.math import Vector2

#screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)
TILE_SIZE = 64


HUD_SCALE = Vector2(1.0, 0.1)
HUD_POS = Vector2(0.0, 0.0)

MENU_SCALE = Vector2(0.7, 0.5)
MENU_POS = SCREEN / 2
MENU_RADIUS = 10


menu_entries ={"Start":None,
                "Options":None,
                "Quit": None
                }