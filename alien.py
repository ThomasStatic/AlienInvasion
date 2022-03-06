import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet (of aliens)"""

	def __init__(self, ai_game):
		"""Initialize the alien and set its starting position"""

		# Initialize the sprite attributes properly
		super().__init__()

		# Inherit screen properites from game
		self.screen = ai_game.screen

		# Load the alien and set its rect attribute
		self.image = pygame.image.load('Images/alien.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's exact horizontal position
		self.x = float(self.rect.x)

		
