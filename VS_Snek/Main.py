import pygame
import random
from Player import Player
from AppleBlock import AppleBlock
SCREEN_FILL = (60,0,0)
WIDTH = 800
HEIGHT = 600
SQUISH = 0
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
screenfill = SCREEN_FILL
quit = False
apples = pygame.sprite.Group()
loc = [random.randint(0, WIDTH-20),random.randint(0,HEIGHT-20)]
x,y = loc[0]-loc[0]%20,loc[1]-loc[1]%20
apple = AppleBlock([x,y], apples)
player = Player((WIDTH/2,HEIGHT/2))
counter = 0
growtimes = 3
def draw():
	apple.draw(screen)
	player.draw(screen)

while not quit:
	events = []
	pressed_keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True
		else: events.append(event)
	screen.fill(SCREEN_FILL)
	pygame.draw.rect(screen, (0,0,0), [SQUISH*counter, SQUISH*counter, WIDTH - SQUISH*counter*2, HEIGHT-SQUISH*counter*2])

	#update
	apples.update()
	if player.collide(apple): 
		player.grow(growtimes)
		apples.empty()
		counter+=1
		player.playBuffer+=SQUISH
		col = True
		while(col):
			loc = [random.randint(counter*SQUISH, WIDTH-20-counter*SQUISH),random.randint(counter*SQUISH,HEIGHT-20-counter*SQUISH)]
			x,y = loc[0]-loc[0]%20,loc[1]-loc[1]%20
			apple = AppleBlock([x,y], apples)
			col = player.body_collide(apple)

	player.update(events, pressed_keys)
	if(player.dead):
		quit = True
		print("YOU LOSE!")
		print("Snake length: " + str(counter*3 + 3))
	draw()

	pygame.display.flip()
	clock.tick(12 + counter)
pygame.quit()
