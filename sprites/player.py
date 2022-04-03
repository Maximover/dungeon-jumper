import pygame

BASE_SPEED = 5.5

class Player(pygame.sprite.Sprite):
    def __init__(self, position) -> None:
        super().__init__()
        self.movement = pygame.math.Vector2(0,0)
        self.image = pygame.Surface((48,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=position)
        self.speed = BASE_SPEED
        self.lifes = 1
        self.gravity = 0.65
        self.jump_strength = -16
        self.keys = 0

    def move(self):
        keys = pygame.key.get_pressed()

        # x axis movement
        if keys[pygame.K_d]:
            self.movement.x = 1
        elif keys[pygame.K_a]:
            self.movement.x = -1
        elif keys[pygame.K_w]:
            pass
        else:
            self.movement.x = 0

        # y axis movement in level.py

    def jump(self):
        self.movement.y = self.jump_strength

    def update(self):
        self.move()

