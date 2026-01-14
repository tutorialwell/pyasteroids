# astroid.py

import pygame
from constants import LINE_WIDTH


from circleshape import CircleShape

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	
	def draw(self, screen: pygame.display):
		"""
		Override of:
			def draw(self, screen: pygame.display):
				pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
		"""
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
	
	def update(self, delta_time):
		self.position += self.velocity * delta_time