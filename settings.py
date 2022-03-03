class Settings:
	"""A class to store all the settings for Alien Invasion"""

	def __init__(self):
		"""Initializes the game's settings"""
		
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_colour = (230, 230, 230)

		# Ship settings
		self.ship_speed = 0.85