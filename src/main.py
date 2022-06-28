import pygame, time, math
from sys import exit

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 20)

# Initialize Diplay Variables 
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = DISPLAY_WIDTH / 12 * 9

# Initialize Simulation Variable
RUNNING = True
TARGET_FPS = 60
fps = 0
prev_time = time.time()
dt = 0

# creates simulation main window
sim_window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))	# creates the main display window
sim_canvas = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))			# creates the canvas which later game screens will be drawn on
pygame.display.set_caption("Ant Simulator")

test_ant = pygame.image.load('img/Ant.png')
test_x = DISPLAY_WIDTH/2
test_y = DISPLAY_HEIGHT/2
test_speed = 1
test_facing = 0

def ant_movement(key, _x, _y, _facing, _speed):
	# TODO replace movement with angle/velocity movement
	# up moves forward, side arrows change angle
	# Note: SOHCAHtoa
	# facing is an int value between 0 and 359, saved to each ant object, 0 is directly right going clockwise
	# sin(theta) = opposite/hypoteneuse
	# sin(facing) = y-displacement/move_speed
	# y-displacement = move_speed * sin(facing)
	# x-displacement = move_speed * cos(facing)
	if key[pygame.K_UP]:
		vel = _speed
	else:
		vel = 0
	if key[pygame.K_LEFT]:
		_facing -= 1
	if key[pygame.K_RIGHT]:
		_facing += 1
	if _facing > 359:
		_facing -= 360
	if _facing < 0:
		_facing += 360

	_x += vel * math.cos(math.radians(_facing))
	_y += vel * math.sin(math.radians(_facing))
	return _x, _y, _facing

# game/sim loop
while RUNNING:
	# Limiting framerate using delta time
	clock.tick(TARGET_FPS)
	now = time.time()
	dt = now - prev_time
	prev_time = now

	# event listeners
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUNNING = False
	
	# testing movement
	# TODO this doesn't work, need to fix it, rotate blit
	test_x, test_y, test_facing = ant_movement(pygame.key.get_pressed(), test_x, test_y, test_facing, test_speed)
	test_ant = pygame.transform.rotate(test_ant, test_facing)

	sim_canvas.fill('gray45')

	fps_text = font.render("FPS: " + str(round(clock.get_fps(), 2)) + "\nFacing: " + str(test_facing), False, (255, 255, 255))

	sim_canvas.blit(fps_text, (0,0))
	sim_canvas.blit(test_ant, (test_x, test_y))

	sim_window.blit(sim_canvas, (0, 0))
	pygame.display.update()
pygame.quit()