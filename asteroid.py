import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_VELOCITY_MULTIPLIER
from logger import log_event

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	
	def draw(self, screen: pygame.display):
		"""Override"""
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
	
	def split(self):
		self.kill()
		
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			new_angle = random.uniform(20.0, 50.0)
			new_raidus = self.radius - ASTEROID_MIN_RADIUS
			asteroid_1_rotation = self.velocity.rotate(new_angle)
			asteroid_2_rotation = self.velocity.rotate(-new_angle)
			
			asteroid_zim = Asteroid(self.position[0], self.position[1], new_raidus)
			asteroid_zim.velocity = asteroid_1_rotation * ASTEROID_VELOCITY_MULTIPLIER

			asteroid_gir = Asteroid(self.position[0], self.position[1], new_raidus)
			asteroid_gir.velocity = asteroid_2_rotation * ASTEROID_VELOCITY_MULTIPLIER			
			
	
	def update(self, delta_time):
		self.position += self.velocity * delta_time