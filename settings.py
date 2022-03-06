class Settings:
	"""A class to store all the settings for Alien Invasion"""

	def __init__(self):
		"""Initializes the game's settings"""
		
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_colour = (75, 0, 130)

		# Ship settings
		self.ship_speed = 0.70

		# Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_colour = (250, 0, 0) # (red)
		self.bullets_allowed = 3
