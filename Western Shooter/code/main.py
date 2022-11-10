import pygame, sys
from pygame.math import Vector2 as vector
from settings import *
from player import Player

class AllSprites(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.offset = vector()
		self.display_surface = pygame.display.get_surface()
		self.bg = pygame.image.load('../graphics/other/bg.png').convert()

	def custmomize_draw(self,player):
		self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
		self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

		self.display_surface.blit(self.bg, -self.offset)

		for sprite in self.sprites():
			offset_rect = sprite.image.get_rect(center = sprite.rect.center)
			offset_rect.center -= self.offset
			self.display_surface.blit(sprite.image, offset_rect)

class Game:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption('Western shooter')
		self.clock = pygame.time.Clock()

		# groups
		self.all_sprites = AllSprites()

		self.setup()

	def setup(self):
		self.player = Player((200,200), self.all_sprites, PATHS['player'], None)

	def run(self):
		while True:
			# event loop
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			dt = self.clock.tick() / 1000

			# update grouops
			self.all_sprites.update(dt)

			# draw groups
			self.display_surface.fill('black')
			self.all_sprites.custmomize_draw(self.player)

			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()