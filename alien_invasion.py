import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


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

		# Create an instance of a ship and its bullets
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		"""Start the main loop of the game"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
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

		if event.key == pygame.K_UP:
			# Move the ship up
			self.ship.moving_up = True

		if event.key == pygame.K_DOWN:
			# Move the ship down
			self.ship.moving_down = True

		if event.key == pygame.K_q:
			# Quit the game if the user presses 'q'
			sys.exit()

		if event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""Responds to keypresses"""
		if event.key == pygame.K_RIGHT:
			# Stop moving the ship to the right
			self.ship.moving_right = False

		if event.key == pygame.K_LEFT:
			# Stop moving the ship to the left
			self.ship.moving_left = False

		if event.key == pygame.K_UP:
			# Stop moving the ship up
			self.ship.moving_up = False

		if event.key == pygame.K_DOWN:
			# Stop moving the ship down
			self.ship.moving_down = False

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group"""

		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update position of bullets and get rid of old bullets"""
		self.bullets.update()

		# Get rid of bullets that have dissapeared
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)



	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen"""

		# Redraw the screen during each pass
		self.screen.fill(self.settings.bg_colour)
		self.ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		# Make the most recently drawn screen visible
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()
