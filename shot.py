# shot.py

import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, SHOT_RADIUS)
	
	def draw(self, screen: pygame.display):
		"""
		Override of CircleShape.draw()
		"""
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
		
	def update(self, delta_time):
		self.position += self.velocity * delta_time