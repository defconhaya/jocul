import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos, group) -> None:
        super().__init__(group)
        self.image = pygame.image.load('gfx/player.png')
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self, keys):
        # keys = pygame.key.get_pressed()
        if keys:
            if keys[pygame.K_UP]:
                self.direction.y = -1
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
            else:
                self.direction.x = 0


    def run(self, keys):
        self.input(keys)
        self.rect.center += self.direction * self.speed

