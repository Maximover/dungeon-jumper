import pygame, os
from res.settings import ASSET_DIR

class Spikes(pygame.sprite.Sprite):
    def __init__(self, position, size) -> None:
        super().__init__()
        self.image = pygame.Surface((size, size/32))
        self.image = pygame.image.load(os.path.join(ASSET_DIR, 'spikes_tall.png'))
        self.rect = self.image.get_rect(bottomleft=position)

    def update(self, move_val):
        self.rect.x += move_val
