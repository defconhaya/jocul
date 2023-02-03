import pygame, sys
from settings import *


class HUD:
    def __init__(self) -> None:
        self.width = SCREEN.x * HUD_SCALE.x
        self.height = SCREEN.y * HUD_SCALE.y
        self.dimensions = pygame.math.Vector2(self.width, self.height)
        self.surf = pygame.display.get_surface()
        self.rect = pygame.Rect(HUD_POS, self.dimensions)
        self.font = pygame.font.Font('font/LycheeSoda.ttf', 20)

 
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def display_info(self):
        player_text_surf = self.font.render('Player keys: Arrow keys', False, 'Black')
        player_text_rect = player_text_surf.get_rect( topleft = (10, 1))
        self.surf.blit(player_text_surf,player_text_rect)
        
        map_text_surf = self.font.render('Map keys: W A S D', False, 'Black')
        map_text_rect = map_text_surf.get_rect(topleft = (10, 15))
        self.surf.blit(map_text_surf,map_text_rect)
        
        menu_text_surf = self.font.render('Menu keys: Esc', False, 'Black')
        menu_text_rect = menu_text_surf.get_rect(topleft = (10, 29))
        self.surf.blit(menu_text_surf,menu_text_rect)


    def run(self, dt):
        #draw hud bkg
        pygame.draw.rect(self.surf, "orange", self.rect, border_radius = HUD_RADIUS)
        self.display_info()
        self.event_loop()
        #update screen
        pygame.display.update()


    