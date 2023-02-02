import pygame, sys
from settings import *
from hud import HUD


class Game:
    def __init__(self) -> None:
                
        pygame.init()        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jocu")
        self.clock = pygame.time.Clock()        
        self.hud = HUD()

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            # pygame.display.update()
            self.hud.run(dt)

if __name__ == '__main__':
    
    game = Game()
    game.run()