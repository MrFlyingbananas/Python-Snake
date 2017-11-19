import pygame
from SnakeBlock import SnakeBlock, BODY_SIDE_LENGTH
from enum import Enum
WIDTH = 800
HEIGHT = 600


class Direction(Enum):
	UP = 0
	DOWN = 1
	LEFT = 2
	RIGHT = 3

class Player():
	def __init__(self, pos):
		self._bodyRender = pygame.sprite.Group()
		self._bodyCollider = pygame.sprite.Group()
		self._body = [SnakeBlock(pos, self._bodyRender)]
		self._dir = Direction.DOWN
		self.dead = False
		self._move = True
		self.playBuffer = 0
		self.grow(2)
	def draw(self, screen):
		self._bodyRender.draw(screen)

	def move_up(self):
		self._body[0].pos[1] -= BODY_SIDE_LENGTH
	def move_down(self):
		self._body[0].pos[1] += BODY_SIDE_LENGTH
	def move_left(self):
		self._body[0].pos[0] -= BODY_SIDE_LENGTH
	def move_right(self):
		self._body[0].pos[0] += BODY_SIDE_LENGTH

		
	def update(self, events, pressed_keys):
		if pressed_keys[pygame.K_w] and self._dir != Direction.DOWN : self._dir = Direction.UP
		elif pressed_keys[pygame.K_s] and self._dir != Direction.UP : self._dir = Direction.DOWN
		elif pressed_keys[pygame.K_a] and self._dir != Direction.RIGHT : self._dir = Direction.LEFT
		elif pressed_keys[pygame.K_d] and self._dir != Direction.LEFT : self._dir = Direction.RIGHT
		if(self._move):
			prevHead = [self._body[0].pos[0],self._body[0].pos[1]]
			if self._dir == Direction.UP:
				self.move_up()
			elif self._dir == Direction.DOWN:
				self.move_down()
			elif self._dir == Direction.LEFT:
				self.move_left()
			elif self._dir == Direction.RIGHT:
				self.move_right()	
			if(self._body[0].pos[1] < self.playBuffer): self._body[0].pos[1] = HEIGHT - self.playBuffer - BODY_SIDE_LENGTH
			if(self._body[0].pos[1] >= HEIGHT - self.playBuffer): self._body[0].pos[1] = self.playBuffer
			if(self._body[0].pos[0] < self.playBuffer): self._body[0].pos[0] = WIDTH - self.playBuffer - BODY_SIDE_LENGTH
			if(self._body[0].pos[0] >= WIDTH - self.playBuffer): self._body[0].pos[0] = self.playBuffer
			
			if len(self._body) > 1:
				removed =  self._body.pop(len(self._body) - 1)
				removed.kill()
				self._body.insert(1, SnakeBlock(prevHead, self._bodyRender, self._bodyCollider))
			self._bodyRender.update()
			if len(pygame.sprite.spritecollide(self._body[0], self._bodyCollider, 0)) > 0: 
				self.dead = True

	def collide(self,sprite):
		return pygame.sprite.collide_rect(self._body[0], sprite)

	def body_collide(self, sprite):
		return len(pygame.sprite.spritecollide(sprite, self._bodyCollider, 0)) > 0

	def grow(self, times=1):
		for i in range(0, times):
			pos = self._body[0].pos
			if self._dir == Direction.UP:
				self._body.insert(1, SnakeBlock((pos[0], pos[1]+BODY_SIDE_LENGTH), self._bodyRender, self._bodyCollider))
				#self._body.append(SnakeBlock((pos[0], pos[1]+BODY_SIDE_LENGTH), self._bodyRender, self._bodyCollider))
			elif self._dir == Direction.DOWN:
				self._body.insert(1, SnakeBlock((pos[0],pos[1]-BODY_SIDE_LENGTH), self._bodyRender, self._bodyCollider))
				#self._body.append(SnakeBlock((pos[0], pos[1]-BODY_SIDE_LENGTH), self._bodyRender, self._bodyCollider))
			elif self._dir == Direction.LEFT:
				self._body.insert(1, SnakeBlock((pos[0]+BODY_SIDE_LENGTH,pos[1]), self._bodyRender, self._bodyCollider))
				#self._body.append(SnakeBlock((pos[0]+BODY_SIDE_LENGTH, pos[1]), self._bodyRender, self._bodyCollider))
			elif self._dir == Direction.RIGHT:
				self._body.insert(1, SnakeBlock((pos[0]-BODY_SIDE_LENGTH-1,pos[1]), self._bodyRender, self._bodyCollider))
				#self._body.append(SnakeBlock((pos[0]-BODY_SIDE_LENGTH, pos[1]), self._bodyRender, self._bodyCollider))
			
		