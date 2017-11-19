import pygame
from SnakeBlock import BODY_SIDE_LENGTH
class AppleBlock(pygame.sprite.Sprite):
	def __init__(self, pos, *groups):
		pygame.sprite.Sprite.__init__(self, groups)
		self.image = pygame.Surface([BODY_SIDE_LENGTH, BODY_SIDE_LENGTH])
		self.image.fill((255,10,10))
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		self.pos = [pos[0], pos[1]]
		
	def draw(self, screen):
		pygame.draw.circle(screen, (255,10,10), [self.pos[0] + int(BODY_SIDE_LENGTH/2), self.pos[1] + int(BODY_SIDE_LENGTH/2)], int(BODY_SIDE_LENGTH/2))
		pygame.draw.ellipse(screen, (0,128,0), [self.pos[0]+ int(BODY_SIDE_LENGTH/2) - 3, self.pos[1] - 5, 6, 6])