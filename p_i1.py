import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

playerImg = pygame.image.load("demon.png")       # Importowanie grafiki bohatera
playerX = 250
playerY = 250
speed = 1

def player(x, y):
	screen.blit(playerImg, (x, y))

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((36, 13, 90))                    

	player(playerX, playerY)	                 # Renderowanie bohatera

	keys = pygame.key.get_pressed()              # Sterowanie klwiszami
	if keys[pygame.K_w]:
		playerY -= speed

	if keys[pygame.K_s]:
		playerY += speed

	if keys[pygame.K_a]:
		playerX -= speed

	if keys[pygame.K_d]:
		playerX += speed

	if playerX <= 0:                             # Granica ekranu
		playerX += speed

	if playerX >= 500 - 64:
		playerX -= speed

	if playerY <= 0:
		playerY += speed

	if playerY >= 500 - 64:
		playerY -= speed


	pygame.display.update()