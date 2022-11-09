import pygame, sys
from settings import *
from player import Player

class Game:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption('Western shooter')
		self.clock = pygame.time.Clock()

		# groups
		self.all_sprites = pygame.sprite.Group()

		self.setup()

	def setup(self):
		Player((200,200), self.all_sprites, None, None)

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
			self.all_sprites.draw(self.display_surface)

			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()