import pygame, sys
from player import Player
from camera import CameraGroup
from timer import Timer
from menu import Menu
from mapObjects import Tree
from random import randint
from settings import *

class Level:
    def __init__(self) -> None:
        self.surface = pygame.display.get_surface()
        self.width = SCREEN.x * (HUD_SCALE.x)
        self.height = SCREEN.y * (1 - HUD_SCALE.y)
        self.dimensions = pygame.math.Vector2(self.width, self.height)
        self.pos = pygame.math.Vector2(0, SCREEN.y * HUD_SCALE.y)
        self.rect = pygame.Rect(self.pos, self.dimensions)
        #camera
        self.camera_group = CameraGroup()
        #player
        self.player = Player(START_POS, self.camera_group)           
        #objects
        for i in range(20):
            random_x = randint(1000,2000)
            random_y = randint(1000,2000)
            Tree((random_x,random_y),self.camera_group)
        #menu
        self.menu = Menu(self.surface)
        #timers
        self.timers = {
        # 'toggle menu': Timer(200)
        }
        self.keys = None



    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def event_loop(self):
        self.keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()            
            # if self.keys[pygame.K_ESCAPE] and not self.menu.timer.active:
            #     self.menu.timer.activate()
            #     self.menu.toggle()
            #     print("menu: ", self.menu.menu_active)


            if event.type == pygame.KEYDOWN:                
                if event.key == pygame.K_ESCAPE and not self.menu.timer.active:                    
                    self.menu.timer.activate()
                    self.menu.toggle()
                    print("menu: ", self.menu.menu_active)


    def run(self, dt):
        self.menu.run(dt)
        self.event_loop()        
        if not self.menu.menu_active:
            self.camera_group.update()
            self.camera_group.custom_draw(self.player, self.keys)
            self.player.run(self.keys)
        
        
        self.event_loop()


