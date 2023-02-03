from settings import *
import pygame

class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, group) -> None:
        super().__init__(group)
        self.image = pygame.image.load('gfx/tree.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

