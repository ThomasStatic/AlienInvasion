import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint

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
		self.aliens = pygame.sprite.Group()
		self.stars = pygame.sprite.Group()

		self._create_stars()
		self._create_fleet()
		

	def run_game(self):
		"""Start the main loop of the game"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_aliens()
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

	def _update_aliens(self):
		"""
		Check if the fleet is at an edge,
		then update the positions of all aliens in the fleet.
		"""
		self._check_fleet_edges()
		self.aliens.update()

	def _create_fleet(self):
		"""Create a fleet of aliens"""

		# Create an alien and find the number of aliens in a row
		# Spacing between each alien is one alien width
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = 1300 - (2*alien_width)
		number_aliens_x = available_space_x//(2*alien_width)

		# Determine the number of rows of aliens that fit on a screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - 
			(3 * alien_height) - ship_height)
		number_rows = available_space_y // (2*alien_height)

		# Create the full fleet of aliens
		for row_number in range(number_rows):
			# Create the first row of aliens
			for alien_number in range(number_aliens_x):
				# Create an alien and place it in the row
				self._create_alien(alien_number, row_number)

	def _create_stars(self):
		"""Create all the background stars"""

		# Create a star and find the number of stars per row
		# Spacing between the stars is 2 star widths
		star = Star(self)
		star_width, star_height = star.rect.size
		available_space_x = 1300 - (2*star_width)
		number_stars_x = available_space_x // (2*star_width)

		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (randint(1,3) * star_height) - ship_height)
		number_rows = available_space_y//(2*star_height)

		# Create all the stars
		for row_number in range(number_rows):
			# Create a single row of stars
			for star_number in range(number_stars_x):
				# Create a star and place it in the row
				self._create_star(star_number, row_number)


	def _create_alien(self, alien_number, row_number):
		"""Create an alien and place it in the row"""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien_height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		"""Respond appropriately if any aliens have reached an edge"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
			break

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet's direction"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1


	def _create_star(self, star_number, row_number):
		"""Create a star and place it in the row"""
		star = Star(self)
		star_width, star_height = star.rect.size
		star.x = star_width + randint(2, 4) * star_width * star_number
		star.rect.x = star.x
		star.rect.y = star_height + randint(2,5) * star.rect.height * row_number
		self.stars.add(star)
		

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen"""

		# Redraw the screen during each pass
		self.screen.fill(self.settings.bg_colour)
		

		
		self.stars.draw(self.screen)
		self.aliens.draw(self.screen)
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.ship.blitme()


		# Make the most recently drawn screen visible
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()
