import sys
import pygame
from timer import Timer
from settings import *
from pygame.math import Vector2 as vector

class Menu:
    def __init__(self, surface) -> None:
        self.entries = menu_entries
        self.display_surface = surface
        self.width = SCREEN.x * MENU_SCALE.x
        self.height = SCREEN.y * MENU_SCALE.y
        self.dimensions = pygame.math.Vector2(self.width, self.height)        
        self.pos = ((SCREEN.x- self.width) / 2, SCREEN.y * HUD_SCALE.y + (SCREEN.y *(1 - HUD_SCALE.y) - self.height) / 2)
        self.rect= pygame.Rect(( (SCREEN.x- self.width) / 2, SCREEN.y * HUD_SCALE.y + (SCREEN.y *(1 - HUD_SCALE.y) - self.height) / 2), self.dimensions)
        self.menu_active = False
        self.timer = Timer(200)
        
    def toggle(self):
        self.menu_active = not self.menu_active
        

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



    def run(self, dt):
        self.event_loop()
        self.timer.update()
        #draw menu
        if self.menu_active:
            pygame.draw.rect(self.display_surface,(0,55,55), self.rect, border_radius = MENU_RADIUS)
            pygame.display.update() 
 
        # s = pygame.Surface(self.dimensions, pygame.SRCALPHA)   # per-pixel alpha
        # s.fill((0,55,50,200))                         # notice the alpha value in the color
        # self.display_surface.blit(s, self.pos)        
