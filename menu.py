import sys
import pygame
from settings import *
from pygame.math import Vector2 as vector

class Menu:
    def __init__(self, surface) -> None:
        self.entries = menu_entries
        self.display_surface = surface
        self.width = SCREEN.x * MENU_SCALE.x
        self.height = SCREEN.y * MENU_SCALE.y
        self.dimensions = pygame.math.Vector2(self.width, self.height)        
        self.rect= pygame.Rect(( (SCREEN.x- self.width) / 2, SCREEN.y * HUD_SCALE.y + (SCREEN.y *(1 - HUD_SCALE.y) - self.height) / 2), self.dimensions)
        

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def run(self, dt):
        
        pygame.draw.rect(self.display_surface,"green", self.rect, border_radius = MENU_RADIUS)
        self.event_loop()        
        pygame.display.update() 
