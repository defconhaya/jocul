import pygame, sys
from timer import Timer
from menu import Menu
from level import Level
from settings import *

class HUD:
    def __init__(self) -> None:
        self.width = SCREEN.x * HUD_SCALE.x
        self.height = SCREEN.y * HUD_SCALE.y
        self.dimensions = pygame.math.Vector2(self.width, self.height)
        self.surf = pygame.display.get_surface()
        self.rect = pygame.Rect(HUD_POS, self.dimensions)

        #menu
        self.menu_active = False
        self.menu = Menu(self.surf)

        #Level
        self.level = Level()

        #timers
        self.timers = {
        'toggle menu': Timer(200)
        }

    def toggle_menu(self):
        self.menu_active = not self.menu_active


    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and not self.timers['toggle menu'].active:
                        self.timers['toggle menu'].activate()                        
                        self.toggle_menu()
                        print("menu: ", self.menu_active)



    def run(self, dt):
        #draw hud        
        pygame.draw.rect(self.surf, "orange", self.rect)

        #draw level
        self.level.run(dt)

        #timers
        self.update_timers()
        self.event_loop()

        #draw menu
        if self.menu_active:
            self.menu.run(dt)

        #update screen
        pygame.display.update()


    