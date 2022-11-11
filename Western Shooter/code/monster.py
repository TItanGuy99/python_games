import pygame 
from entity import Entity
from pygame.math import Vector2 as vector

class Monster:
    def get_player_distance_direction(self):
        enemy_pos = vector(self.rect.center)
        player_pos = vector(self.player.rect.center)
        distance = (player_pos - enemy_pos).magnitude()

        if distance != 0:
            direction = (player_pos - enemy_pos).normalize()
        else:
            direction = vector()

        return (distance, direction)

    def face_player(self):
        distance, direction = self.get_player_distance_direction()

        if distance < self.notice_radius:
            if -0.5 < direction.y < 0.5:
                if direction.x < 0: # player to the left
                    self.status = 'left_idle'
                elif direction.x > 0: # player to the right
                    self.status = 'right_idle'
            else: 
                if direction.y < 0: # player to the top
                    self.status = 'up_idle'
                elif direction.y > 0: # player to the bottom
                    self.status = 'down_idle'

    def walk_to_player(self):
        distance, direction = self.get_player_distance_direction()
        if self.attack_radius < distance < self.walk_radius:
            self.direction = direction
            self.status = self.status.split('_')[0]
        else:
            self.direction = vector()

class Coffin(Entity, Monster):
    def __init__(self, pos, groups, path, collision_sprites, player):
        super().__init__(pos, groups, path, collision_sprites)

        # overwrites
        self.speed = 150

        # player interaction
        self.player = player
        self.notice_radius = 550
        self.walk_radius = 400
        self.attack_radius = 50

    def animate(self,dt):
        current_animation = self.animations[self.status]
        self.frame_index += 7 * dt

        if self.frame_index >= len(current_animation):
            self.frame_index = 0

        self.image = current_animation[int(self.frame_index)]            

    def update(self, dt):
        self.face_player()
        self.walk_to_player()
        self.move(dt)
        self.animate(dt)


class Cactus(Entity, Monster):
    def __init__(self, pos, groups, path, collision_sprites, player):
        super().__init__(pos, groups, path, collision_sprites)
        self.player = player
        self.notice_radius = 600
        self.walk_radius = 500
        self.attack_radius = 350    
        self.speed = 90    

    def animate(self,dt):
        current_animation = self.animations[self.status]
        self.frame_index += 7 * dt

        if self.frame_index >= len(current_animation):
            self.frame_index = 0

        self.image = current_animation[int(self.frame_index)]

    def update(self, dt):
        self.face_player()
        self.walk_to_player()
        self.move(dt)
        self.animate(dt)