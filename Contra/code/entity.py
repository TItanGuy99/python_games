import pygame
from pygame.math import Vector2 as vector
from settings import *
from os import walk

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, path, groups, shoot):
        super().__init__(groups)

        # graphics setup
        self.import_assets(path)
        self.frame_index = 0
        self.status = 'right'

        # image setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()
        self.z = LAYERS['Level']

        # float based movement
        self.direction = vector()
        self.pos = vector(self.rect.topleft)
        self.speed = 400

        # shooting setup
        self.shoot = shoot
        self.can_shoot = True
        self.shoot_time = None
        self.cooldown = 200
        self.duck = False        

    def animate(self, dt):
        self.frame_index += 7 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        
        self.image = self.animations[self.status][int(self.frame_index)]

    def shoot_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time -self.shoot_time > self.cooldown:
                self.can_shoot = True                            

    def import_assets(self, path):
        self.animations = {}
        for index, folder in enumerate(walk(path)):
            if index == 0:
                for name in folder[1]:
                    self.animations[name] = []
            else:
                for file_name in sorted(folder[2], key = lambda string: int(string.split('.')[0])):
                    path = folder[0].replace('\\', '/') + '/' + file_name
                    surf = pygame.image.load(path).convert_alpha()
                    key = folder[0].split('\\')[1]
                    self.animations[key].append(surf)