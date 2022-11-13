import pygame
from settings import *
from pygame.math import Vector2 as vector

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((40, 80))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft = pos)
        self.z = LAYERS['Level']

        # float based movement
        self.direction = vector()
        self.pos = vector(self.rect.topleft)
        self.speed = 400

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def move(self, dt):
        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)

    def update(self, dt):
        self.input()
        self.move(dt)