import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	"""A class to manage stars to add background ambience"""

	def __init__(self, ai_game):
		"""Initialize attributes and set initial position of star"""

		# Inherit sprite properties
		super().__init__()

		# Inherit screen properties from game
		self.screen = ai_game.screen
		
		# Load the image and set its rect attributes
		self.image = pygame.image.load('Images/star_resized.bmp')
		self.rect = self.image.get_rect()

		# Start each new star near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the star's exact horizontal postion
		self.x = float(self.rect.x)