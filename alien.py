import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet (of aliens)"""

	def __init__(self, ai_game):
		"""Initialize the alien and set its starting position"""

		# Initialize the sprite attributes properly
		super().__init__()

		# Inherit properites from game
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the alien and set its rect attribute
		self.image = pygame.image.load("C:/Users/Thomas/OneDrive - Queen's University/Documents/GitHub/Alien Invasion/Images/alien.bmp")
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's exact horizontal position
		self.x = float(self.rect.x)

	def check_edges(self):
		"""Return True if an alien is at the edge of the screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= 350 or self.rect.left <= 0:
			return True	

	def update(self):
		"""Move the alien to the right"""
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x

		

