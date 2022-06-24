import pygame, time
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

test_surface = pygame.Surface((32,32))
test_surface.fill('Red')
test_x = DISPLAY_WIDTH/2
test_y = DISPLAY_HEIGHT/2
test_speed = 4

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
	key_event = pygame.key.get_pressed()
	if key_event[pygame.K_UP]:
		test_y -= test_speed
	if key_event[pygame.K_DOWN]:
		test_y += test_speed
	if key_event[pygame.K_LEFT]:
		test_x -= test_speed
	if key_event[pygame.K_RIGHT]:
		test_x += test_speed


	fps_text = font.render("FPS: " + str(round(clock.get_fps(), 2)), False, (255, 255, 255))

	sim_canvas.fill((0, 0, 0))
	sim_canvas.blit(fps_text, (0,0))
	sim_canvas.blit(test_surface, (test_x, test_y))

	sim_window.blit(sim_canvas, (0, 0))
	pygame.display.update()
pygame.quit()