import pygame
from constants import LINE_WIDTH

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
	def __init__(self, x, y, radius):
		# we will be using this later
		if hasattr(self, "containers"):
			super().__init__(self.containers)
		else:
			super().__init__()

		self.position = pygame.Vector2(x, y)
		self.velocity = pygame.Vector2(0, 0)
		self.radius = radius
		
	def collides_with(self, other):
		distance_between_circles = self.position.distance_to(other.position)
		radius_of_circles = self.radius + other.radius
		
		if distance_between_circles <= radius_of_circles:
			return True
		else:
			return False

	def draw(self, screen: pygame.display):
		pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

	def update(self, dt):
		# must override
		pass