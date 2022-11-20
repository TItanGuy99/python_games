import pygame
from settings import *
from pygame.math import Vector2 as vector

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, surf, direction, groups):
        super().__init__(groups)


        self.image = surf
        if direction.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['Level']

        # float based movement
        self.direction = direction
        self.speed = 1200
        self.pos = vector(self.rect.center)

        self.start_time = pygame.time.get_ticks()

    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

        if pygame.time.get_ticks() - self.start_time > 1000:
            self.kill()