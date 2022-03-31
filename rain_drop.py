import pygame
from pygame.sprite import Sprite

class Rain_Drop(Sprite):
	"""Class to experiment with putting rain drops in AI background"""

	def __init__(self, ai_game):
		"""Initialize all attributes of the rain drop"""

		# Inherit Sprite properties
		super().__init__()

		# Inherit properties from game
		self.screen = ai_game.screen

		# Load the image and set its rect
		self.image = pygame.image.load("Images/rain_drop.bmp")
		self.rect = self.image.get_rect()


		# Start each raindrop at the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the float value of the star's position
		self.x = float(self.rect.x)

	def _check_bottom(self):
		"""Check to see if the rain drop has reached the bottom of the screen"""
		if self.rect.bottom <= 0:
			return True
			