from tkinter.tix import Tree
import pygame
from res.menu import Menu
from res.settings import *
from res.levels import *
from sprites.tile import Tile
from sprites.level import Level

pygame.init()
pygame.display.set_caption('Dungeon jumper')
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
menu = Menu(display, 'menu')
level1 = Level(level1, display, menu)
menu.current_level = level1

while True:
    #play level
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    display.fill('black')
    while menu.intro:
        menu.game_intro()
    level1.run()
    clock.tick(FPS)
    pygame.display.update()
