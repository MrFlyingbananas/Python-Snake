import pygame
import random
BODY_SIDE_LENGTH = 20
class SnakeBlock(pygame.sprite.Sprite):
	
	def __init__(self, pos, *groups):
		pygame.sprite.Sprite.__init__(self, groups)
		self.image = pygame.Surface([BODY_SIDE_LENGTH, BODY_SIDE_LENGTH])
		self.image.fill((random.randint(0,255),255,10))
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		self.pos = [pos[0], pos[1]]
		
	def update(self):
		self.rect.x = self.pos[0]
		self.rect.y = self.pos[1]