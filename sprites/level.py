from platform import platform
import pygame, random
from sprites.door import Door
from sprites.key import Key

from sprites.spikes import Spikes
from .tile import Tile
from .player import Player, BASE_SPEED
from res.settings import *

class Level:
    def __init__(self, level_layout, surface, menu_instance) -> None:
        self.surface = surface
        self.camera_movement_speed = 0
        self.menu_instance = menu_instance
        self.setup_level(level_layout)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.spikes = pygame.sprite.Group()
        self.key = pygame.sprite.Group()
        self.door = pygame.sprite.Group()
        for index_row, row in enumerate(layout):
            for index_col, cell in enumerate(row):
                x = index_col * TILE
                y = index_row * TILE
                if cell == 'X':
                    tile = Tile((x, y), TILE)
                    self.tiles.add(tile)
                if cell == 'P':
                    self.playerObj = Player((x, y))
                    self.player.add(self.playerObj)
                if cell == '_':
                    spikes = Spikes((x, y+TILE), TILE)
                    self.spikes.add(spikes)
                if cell == 'K':
                    key = Key((x, y), TILE)
                    self.key.add(key)
                if cell == 'D':
                    door = Door((x, y), TILE)
                    self.door.add(door)

    def camera_movement(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        move_x = player.movement.x

        if player_x < WIDTH / 3 and move_x < 0:
            self.camera_movement_speed = BASE_SPEED
            player.speed = 0
        elif player_x > WIDTH - (WIDTH / 3) and move_x > 0:
            self.camera_movement_speed = -BASE_SPEED
            player.speed = 0
        else:
            self.camera_movement_speed = 0
            player.speed = 8

    def vertical_collision(self):
        player = self.player.sprite

        # gravity
        try:
            player.movement.y += player.gravity
            player.rect.y += player.movement.y
        
            for sprite in self.spikes:
                if sprite.rect.colliderect(player.rect):
                    self.playerObj.lifes = 0
                    player.kill()
                    self.menu_instance.type = 'death'
                    self.menu_instance.intro = True
                    return

            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.movement.y > 0:
                        keys = pygame.key.get_pressed()
                        player.rect.bottom = sprite.rect.top
                        player.movement.y = 0
                        if keys[pygame.K_SPACE]:
                            player.jump()
                    elif player.movement.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.movement.y = 0
        except:
            pass

        

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.movement.x * player.speed
        
        for sprite in self.spikes:
            if sprite.rect.colliderect(player.rect):
                self.playerObj.lifes = 0
                player.kill()
                self.menu_instance.type = 'death'
                self.menu_instance.intro = True

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.movement.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.movement.x > 0:
                    player.rect.right = sprite.rect.left

        for sprite in self.key:
            if sprite.rect.colliderect(player.rect):
                sprite.kill()
                player.keys += 1
        for sprite in self.door:
            if sprite.rect.colliderect(player.rect) and player.keys == 1:
                player.keys = 0
                self.menu_instance.type = 'win'
                self.menu_instance.intro = True

    def run(self):
        self.tiles.update(self.camera_movement_speed)
        for instance in self.tiles:
            self.surface.blit(instance.image, instance.rect)
        self.spikes.update(self.camera_movement_speed)
        for instance in self.spikes:
            self.surface.blit(instance.image, instance.rect)
        self.key.update(self.camera_movement_speed)
        for instance in self.key:
            self.surface.blit(instance.image, instance.rect)
        self.door.update(self.camera_movement_speed)
        for instance in self.door:
            self.surface.blit(instance.image, instance.rect)

        self.camera_movement()

        self.player.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.player.draw(self.surface)
