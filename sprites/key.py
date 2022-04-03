import pygame, os
from res.settings import ASSET_DIR

class Key(pygame.sprite.Sprite):
    def __init__(self, position, size) -> None:
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image = pygame.image.load(os.path.join(ASSET_DIR, 'key.png'))
        self.rect = self.image.get_rect(topleft=position)

    def update(self, move_val):
        self.rect.x += move_val