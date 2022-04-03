import pygame, sys
from res.settings import *

class Menu:
    def __init__(self, display, screen_type):
        self.intro = True
        self.display = display
        self.clock = pygame.time.Clock()
        self.type = screen_type
        self.current_level = None

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0,0,0))
        return textSurface, textSurface.get_rect()

    def show_menu(self):
        self.display.fill((0,0,0))
        text1 = pygame.font.Font('freesansbold.ttf',75).render('Dungeon Jumper', True, (255,255,255))
        text1_rect = text1.get_rect(center=(WIDTH/2, 150))
        text2 =  pygame.font.Font('freesansbold.ttf',48).render('> Press P to start <', True, (255,255,255))
        text2_rect = text2.get_rect(center=(WIDTH/2, 450))
        text3 =  pygame.font.Font('freesansbold.ttf',24).render('Made by: Wojciech Pela', True, (253, 255, 252))
        text3_rect = text2.get_rect(center=(WIDTH - WIDTH/16, 800))
        self.display.blit(text1, text1_rect)
        self.display.blit(text2, text2_rect)
        self.display.blit(text3, text3_rect)

#biuro@dev.pl
    def show_death_screen(self):
        self.display.fill((255, 0, 34))
        text1 = pygame.font.Font('freesansbold.ttf',75).render('You died', True, (253, 255, 252))
        text1_rect = text1.get_rect(center=(WIDTH/2, 150))
        text2 =  pygame.font.Font('freesansbold.ttf',48).render('> Press R to restart <', True, (253, 255, 252))
        text2_rect = text2.get_rect(center=(WIDTH/2, 450))
        self.display.blit(text1, text1_rect)
        self.display.blit(text2, text2_rect)

    def show_win_screen(self):
        self.display.fill((1, 22, 39))
        text1 = pygame.font.Font('freesansbold.ttf',75).render('You escaped', True, (253, 255, 252))
        text1_rect = text1.get_rect(center=(WIDTH/2, 150))
        text2 =  pygame.font.Font('freesansbold.ttf',48).render('> Press R to restart <', True, (253, 255, 252))
        text2_rect = text2.get_rect(center=(WIDTH/2, 450))
        text3 =  pygame.font.Font('freesansbold.ttf',48).render('> Press M to go to menu <', True, (253, 255, 252))
        text3_rect = text2.get_rect(center=(WIDTH/2, 750))
        self.display.blit(text1, text1_rect)
        self.display.blit(text2, text2_rect)
        self.display.blit(text3, text3_rect)

    def game_intro(self):
        while self.intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p or event.key == pygame.K_r:
                        self.current_level.setup_level(level1)
                        self.intro = False
                    if event.key == pygame.K_m:
                        self.type = 'menu'
                    
            if self.type == 'menu':
                self.show_menu()
            if self.type == 'death':
                self.show_death_screen()
            if self.type == 'win':
                self.show_win_screen()

            pygame.display.update()
            self.clock.tick(15)
        