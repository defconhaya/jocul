import pygame, sys
from settings import *

class Level:
    def __init__(self) -> None:
        self.surface = pygame.display.get_surface()
        self.width = SCREEN.x * (HUD_SCALE.x)
        self.height = SCREEN.y * (1 - HUD_SCALE.y)
        self.dimensions = pygame.math.Vector2(self.width, self.height)
        self.pos = pygame.math.Vector2(0, SCREEN.y * HUD_SCALE.y)
        self.rect = pygame.Rect(self.pos, self.dimensions)

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self, dt):
        pygame.draw.rect(self.surface, "black", self.rect)
        # self.event_loop()


