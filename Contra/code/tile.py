import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z

class CollisionTile(Tile):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups, LAYERS['Level'])
        self.old_rect = self.rect.copy()