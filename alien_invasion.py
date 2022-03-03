import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
	"""Overall class to manage game assets and behaviors"""

	def __init__(self):
		"""Initialize the game and create game resources"""
		pygame.init()
		self.settings = Settings()

		# Custom width window:
		# self.screen = pygame.display.set_mode(
		# (self.settings.screen_width, self.settings.screen_height))

		# Full screen:
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_width = self.screen.get_rect().height

		pygame.display.set_caption("Alien Invasion")

		# Create an instance of a ship
		self.ship = Ship(self)

	def run_game(self):
		"""Start the main loop of the game"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()

	def _check_events(self):
		"""Respond to key presses and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			# If a key is pressed
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
				

			# If a key is lifted		
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Responds to keypresses"""
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right
			self.ship.moving_right = True

		if event.key == pygame.K_LEFT:
			# Move the ship to the left
			self.ship.moving_left = True

		if event.key == pygame.K_q:
			# Quit the game if the user presses 'q'
			sys.exit()

	def _check_keyup_events(self, event):
		"""Responds to keypresses"""
		if event.key == pygame.K_RIGHT:
			#Stop moving the ship to the right
			self.ship.moving_right = False

		if event.key == pygame.K_LEFT:
			# Stop moving the ship to the left
			self.ship.moving_left = False



	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen"""

		# Redraw the screen during each pass
		self.screen.fill(self.settings.bg_colour)
		self.ship.blitme()

		# Make the most recently drawn screen visible
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()
