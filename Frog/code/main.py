import pygame, sys
from setting import *
from player import Player

# basic setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

# groups
all_sprites = pygame.sprite.Group()

# sprites
player = Player((600, 400), all_sprites)

# game loop
while True:
    
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw a bg
    display_surface.fill('black')

    # delta time
    dt = clock.tick() / 1000

    #update
    all_sprites.update(dt)

    # draw
    all_sprites.draw(display_surface)

    # update the display surface -> drawing the frame
    pygame.display.update()
